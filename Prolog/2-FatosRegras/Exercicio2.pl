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

%agrupamento de fatos importante para melhor desempenho
%o nome que vem primeiro se chama functor
%aridade é a quantidade de argumentos dentro de um functor