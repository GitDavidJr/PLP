:- dynamic sala/6.

%sala(num,dia,inicio,fim,discipl,tipo)
sala(cp1103, seg, 10, 13, aaa, p).
sala(cp2301, ter, 10, 11, aaa, p).
sala(di011, sab, 12, 10, aaa, p). %erro
sala(cp3204, dom, 8, 10, aaa, p).
sala(di011, sex, 14, 16, aaa, p).
sala(cp204, sab, 15, 17, aaa, p).
sala(di011, qui, 14, 13, aaa, p). %erro
sala(di104, qui, 9, 10, aaa, p).
sala(dia1, dom, 14, 16, aaa, p).
sala(cp1220, sab, 14, 18, aaa, p).


% listing(sala).

% (sala(_,_,Ini,Fim,_,_),Ini > Fim),retractall(sala(_,_,Ini,Fim,_,_)).

% listing(sala).

% assert(sala(di011, sab, 10, 12, aaa, p)).

% assert(sala(di011, qui, 13, 14, aaa, p)).