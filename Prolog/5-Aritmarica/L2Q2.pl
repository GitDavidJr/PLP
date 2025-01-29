nota(joao, 5.0).
nota(maria, 6.0).
nota(joana, 8.0).
nota(mariana, 9.0).
nota(cleuza, 0.5).
nota(jose, 6.5).
nota(jaoquim, 4.5).
nota(mara, 4.0).
nota(mary, 10.0).

diario(X) :-nota(X,Nota),(
                            (Nota>=7,write('Aprovado'));
                            (Nota<7,Nota>=5,write('Recuperação'));
                            (Nota<7,write('Reprovado'))
                         ).