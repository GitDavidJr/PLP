aluno(joao, calculo).
aluno(maria, calculo).
aluno(joel, programacao).
aluno(joel, estrutura).
frequenta(joao, puc).
frequenta(maria, puc).
frequenta(joel, ufrj).
professor(carlos, calculo).
professor(ana_paula, estrutura).
professor(pedro, programacao).
funcionario(pedro, ufrj).
funcionario(ana_paula, puc).
funcionario(carlos, puc).

sao_alunos_do_professor(A,X) :- professor(X, Materias), aluno(A, Materias).

associados(Pessoa, Faculdade) :- frequenta(Pessoa, Faculdade);funcionario(Pessoa, Faculdade).