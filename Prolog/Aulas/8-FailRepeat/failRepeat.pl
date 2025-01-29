aluno(marcelo).
aluno(andre).
aluno(roberto).

escreverSemFail :- aluno(X), write(X).
escreverComFail :- aluno(X), write(X), nl, fail.

% repeat, write(ola),nl,fail.

adivinhe_numero :- 
                    N is random(5) + 1,
                    repeat,
                       lerDados(G),
                       processarDados(G, N).
            
lerDados(G) :- write('Entre com um numero (1 ate 5): '),
               read(G).

processarDados(G, N) :- G =:= N, write('Voce acertou'),nl,!.
processarDados(_,_) :- write("Errou"),nl, fail.

repeatPalavra :- repeat,
                 write('Digite uma palabra: '),
                 read(Palavra),
                 (
                    Palavra == fim -> !;
                    processarPalabra(Palavra), fail
                 ).
                 

processarPalabra(Palavra) :- write('===> '), write(Palavra),nl.