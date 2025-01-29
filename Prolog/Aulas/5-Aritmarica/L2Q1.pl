maiorQueCem() :- write('Entre com o número:'),
                 read(X),
                 (
                    (X>100,write('O número é maior que cem'))
                    ;
                    (X<100),write('O número e menor que cem')
                    ;
                    (X=:= 100),write('O número é igual a cem')
                 ).