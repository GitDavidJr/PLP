imc(Peso, Altura) :- X is Peso/ (Altura*Altura),
                     write('Seu IMC é: '),write(X).