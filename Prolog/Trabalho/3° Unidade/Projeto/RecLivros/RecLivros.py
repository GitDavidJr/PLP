from pyswip import Prolog

p = Prolog()

generos = [
    "romance", "classico", "drama", "ficcao", "distopia", "fantasia", 
    "aventura", "satira", "realismo magico", "infantil", "tragedia", 
    "epico", "horror", "poema", "suspense", "misterio", "inspiracional"
]

autores = [
    "Machado de Assis", "Emily Bronte", "George Orwell", "Jane Austen", 
    "J.R.R. Tolkien", "Herman Melville", "Gabriel Garcia Márquez", 
    "Antoine de Saint-Exupéry", "Franz Kafka", "Fyodor Dostoevsky", 
    "William Shakespeare", "Homero", "Bram Stoker", "Mary Shelley", 
    "Dante Alighieri", "Victor Hugo", "F. Scott Fitzgerald", "Aldous Huxley", 
    "Thomas Mann", "Harper Lee", "Charlotte Bronte", "Lewis Carroll", 
    "Dan Brown", "J.K. Rowling", "Paulo Coelho", "Rick Riordan", "Suzanne Collins"
]

def stringValida(nome):
    if ' ' in nome: 
        return f'"{nome}"'  
    return nome  

#base de livros
p.assertz('livro("Dom Casmurro", [genero(romance), genero(classico), autor("Machado de Assis"), ano(1899)])')
p.assertz('livro("O Morro dos Ventos Uivantes", [genero(romance), genero(drama), autor("Emily Bronte"), ano(1847)])')
p.assertz('livro("1984", [genero(ficcao), genero(distopia), autor("George Orwell"), ano(1949)])')
p.assertz('livro("Orgulho e Preconceito", [genero(romance), genero(classico), autor("Jane Austen"), ano(1813)])')
p.assertz('livro("O Senhor dos Aneis", [genero(fantasia), genero(aventura), autor("J.R.R. Tolkien"), ano(1954)])')
p.assertz('livro("Moby Dick", [genero(aventura), genero(classico), autor("Herman Melville"), ano(1851)])')
p.assertz('livro("A Revolucao dos Bichos", [genero(ficcao), genero(satira), autor("George Orwell"), ano(1945)])')
p.assertz('livro("Cem Anos de Solidao", [genero(ficcao), genero(realismo_magico), autor("Gabriel Garcia Marquez"), ano(1967)])')
p.assertz('livro("O Pequeno Principe", [genero(ficcao), genero(infantil), autor("Antoine de Saint-Exupery"), ano(1943)])')
p.assertz('livro("A Metamorfose", [genero(ficcao), genero(drama), autor("Franz Kafka"), ano(1915)])')
p.assertz('livro("Crime e Castigo", [genero(drama), genero(classico), autor("Fyodor Dostoevsky"), ano(1866)])')
p.assertz('livro("Hamlet", [genero(drama), genero(tragedia), autor("William Shakespeare"), ano(1603)])')
p.assertz('livro("Iliada", [genero(epico), genero(classico), autor("Homero"), ano(-750)])')
p.assertz('livro("Odisseia", [genero(epico), genero(aventura), autor("Homero"), ano(-700)])')
p.assertz('livro("Dracula", [genero(horror), genero(classico), autor("Bram Stoker"), ano(1897)])')
p.assertz('livro("Frankenstein", [genero(horror), genero(ficcao), autor("Mary Shelley"), ano(1818)])')
p.assertz('livro("A Divina Comedia", [genero(epico), genero(poema), autor("Dante Alighieri"), ano(1320)])')
p.assertz('livro("Os Miseraveis", [genero(drama), genero(classico), autor("Victor Hugo"), ano(1862)])')
p.assertz('livro("O Grande Gatsby", [genero(drama), genero(classico), autor("F. Scott Fitzgerald"), ano(1925)])')
p.assertz('livro("Admiravel Mundo Novo", [genero(ficcao), genero(distopia), autor("Aldous Huxley"), ano(1932)])')
p.assertz('livro("A Montanha Magica", [genero(ficcao), genero(classico), autor("Thomas Mann"), ano(1924)])')
p.assertz('livro("O Sol e para Todos", [genero(drama), genero(classico), autor("Harper Lee"), ano(1960)])')
p.assertz('livro("Jane Eyre", [genero(romance), genero(drama), autor("Charlotte Bronte"), ano(1847)])')
p.assertz('livro("Alice no Pais das Maravilhas", [genero(fantasia), genero(infantil), autor("Lewis Carroll"), ano(1865)])')
p.assertz('livro("Memorias Postumas de Bras Cubas", [genero(romance), genero(classico), autor("Machado de Assis"), ano(1881)])')
p.assertz('livro("O Codigo Da Vinci", [genero(suspense), genero(misterio), autor("Dan Brown"), ano(2003)])')
p.assertz('livro("Harry Potter e a Pedra Filosofal", [genero(fantasia), genero(infantil), autor("J.K. Rowling"), ano(1997)])')
p.assertz('livro("O Alquimista", [genero(ficcao), genero(inspiracional), autor("Paulo Coelho"), ano(1988)])')
p.assertz('livro("Percy Jackson e o Ladrao de Raios", [genero(fantasia), genero(aventura), autor("Rick Riordan"), ano(2005)])')
p.assertz('livro("Jogos Vorazes", [genero(ficcao), genero(distopia), autor("Suzanne Collins"), ano(2008)])')

#busca por livros
p.assertz('car(Caracteristica, Livros) :- findall(Titulo, ( livro(Titulo, Caracteristicas), member(Caracteristica, Caracteristicas)), Livros)')

def rec(list_pref):

    perceCaract = 100/len(list_pref)

    resultadoQ = []  
    resultadoP = []
    resultadoF = []
    
    for caract in list_pref:
        tipo = ""

        if caract in generos:
            tipo = "genero"
        else:
            tipo = "autor"

        caract = stringValida(caract)
        
        consulta = list(p.query(f'car({tipo}({caract}),X)'))

        
        for dicionario in consulta:
            dicionario['X'] = [item.decode() for item in dicionario['X']]
        
        #print(consulta)

        for dicionario in consulta:
            resultadoQ.append(dicionario['X'])

    
    for i in resultadoQ:
        for j in i:
            found = False
            for k in resultadoP:
                if k[0] == j:
                    k[1] += perceCaract
                    found = True
                    break

            if not found:
                resultadoP.append([j, perceCaract])

    for livro in resultadoP:
        livro_nome = f'"{livro[0]}"'  
        consulta = list(p.query(f'livro({livro_nome},X)'))  

        for item in consulta:
            
            generosT = []
            autor = ""
            ano = ""

            for caracteristica in item['X']:
                if "genero" in caracteristica:
                    generosT.append(caracteristica.split('(')[1].split(')')[0])  
                elif "autor" in caracteristica:
                    autor = caracteristica.split('(')[1].split(')')[0]  
                    autor = autor[2:-1]  
                elif "ano" in caracteristica:
                    ano = caracteristica.split('(')[1].split(')')[0]  

            
            resultadoF.append([livro[0], generosT, autor, int(ano), livro[1]])

    return resultadoF
        

pref = "romance"

list_pref = pref.split(", ")  
        
recomendacao = rec(list_pref)

for item in recomendacao:
        print(item)




