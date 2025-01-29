doa(a,a).
doa(a,ab).
doa(b,b).
doa(b,ab).
doa(ab,ab).
doa(o,a).
doa(o,b).
doa(o,ab).
doa(o,o).

recebe(A,B) :- doa(B,A).