pertence(X,[X|_]).
pertence(X,[_|T]) :- pertence(X,T).

eh_ultima(X,[X]).
eh_ultima(X,[_|T]) :- eh_ultima(X,T).

consecutivos(X,Y,[X,Y|_]).
consecutivos(X,Y,[_|T]) :- consecutivos(X,Y,T).

tamanho([], 0).
tamanho([_|T],Tam) :- tamanho(T,Tam1), Tam is 1 + Tam1.