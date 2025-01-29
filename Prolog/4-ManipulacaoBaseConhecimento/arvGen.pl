:-dynamic mulher/1.
:-dynamic homem/1.
:-dynamic genitor/2.

% assert/1 - acrescenta o fato/regra como ultimo item do rpecicado
% asserta/1 - acrescenta o fato/regra como primeiro item do precicado

% retract/1 remove da base de conhecimento a primeira cláusula (fato ou regra)
%que unifica com o termo q é usado como parametro;

% retractall/1 remove da base cde conhecimento todos os fatos ou regras cuju
%cláusula (fato ou regra) unifique com o termo que é passado como parámetro

% abolish/1 remove da base de conhecimento todos os fatos e regras pelo nome%da regra %ou fato/aridade que é passada como parâmetro (são removidos predicados estáticostambem)

% abolish/2 semelhante a abolish/1, mas passando o nome do fato/regra e a sua
%aridade separadamente (são removidos pedicados esáticos tambem)

mulher(pam).
mulher(ana).
mulher(liz).
mulher(pat).
homem(tom).
homem(bob).
homem(jim).
genitor(pam, bob). % functor = genitor | argumento = pam e bob | aridade = 2
genitor(tom, bob).
genitor(tom, liz).
genitor(bob, ana).
genitor(bob, pat).
genitor(pat, jim).
prole(X, Y) :- genitor(Y, X).