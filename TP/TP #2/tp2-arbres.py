from abe import *
#Ex.2
A1 = arbre('+', arbre('*', 1, 2), arbre('/', arbre('+', 3, 4), 5))
print(fg(A1))