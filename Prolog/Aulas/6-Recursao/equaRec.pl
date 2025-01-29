recorrencia(1,2).
recorrencia(N,Result) :- N >= 2,
                         N1 is N - 1,
                         recorrencia(N1,Result1),
                         Result is Result1 - 3 * (N*N).