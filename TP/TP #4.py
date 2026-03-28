from abe import *
from TP_3 import *
from lc import * 

#Ex.1

def approx_pi(A):
    if est_feuille(A):
        if A == "Pi":
            return 3.14
        return A
    else:
        g = fg(A)
        d = fd(A)
        return arbre(racine(A), approx_pi(g), approx_pi(d))

#print(">>>",approx_pi(arboriser('1+Pi')))

def negation(A):
    if est_feuille(A):
        return -A
    else:
        if racine(A) == '*' or racine(A) == '/':
            g = fg(A)
            d = negation(fd(A))
            return arbre(racine(A), negation(g), negation(d))
        elif racine(A) == '-':
            g = fg(A)
            d = fd(A)
            return arbre(racine(A), d, g)
        else:
            g = fg(A)
            d = fd(A)
            return arbre(racine(A), negation(g), negation(d))

#print('>>>', negation(arboriser('1-3')))

#Ex.2

class Pile:
    def __init__(self,taille):
        self.taille= taille
        self.tableau = taille * [None]
        self.sommet = 0

    def __repr__(self):
        res = "["
        for i in range(self.sommet):
            res += f"{self.tableau[i]} ["
        return res
    
    def push(self,x):
        if self.taille == self.sommet:
            raise "Err push"
        else:
            self.tableau[self.sommet] = x
            self.sommet += 1

    def pop(self):
        if self.sommet == 0:
            raise "Err pop"
        else:
            self.sommet -= 1
            return self.tableau[self.sommet]
        
p = Pile(5)
#print(p)
for i in range(5):
    p.push(i)
    #print(p)

for i in range(5):
    x = p.pop()
    #print(x,p)

#Ex.3


class Pile_lc:
    def __init__(self):
        self.lc = vide()

    def __repr__(self):
        return self.afficher(self.lc)
    
    def afficher(self, x):
        if is_empty(x):
            return "("
        else:
            return self.afficher(tail(x))  + str(head(x)) + "("

    def push(self,x):
        self.lc = liste(x, self.lc)
        
    def pop(self):
        tmp = head(self.lc)
        self.lc = tail(self.lc)
        return tmp

p_lc = Pile_lc()
print(p_lc)
for i in range(10):
    p_lc.push(i)
    print(p_lc)

for i in range(10):
    x = p_lc.pop()
    print(x,p_lc)