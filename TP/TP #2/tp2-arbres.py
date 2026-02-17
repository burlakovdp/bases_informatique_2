from abe import *
#Ex.2
test_arbre = arbre('+', arbre('*', 1, 2), arbre('/', arbre('+', 3, 4), 5))

#Ex.3
A1 = arbre('+', arbre('*', 1, 4), arbre('/', arbre('+', 1, 1), 42))

def contient42(A):
    if est_feuille(A):
        if A == 42:
            return True
        return False
    else:
        g = contient42(fg(A))
        d = contient42(fd(A))
        return g or d
    
#print(contient42(A1))

def compte_paire(A):
    if est_feuille(A):
        if A % 2 == 0:
            return 1
        else:
            return 0
    else:
        g = compte_paire(fg(A))
        d = compte_paire(fd(A))
    return g + d

#print(compte_paire(A1))


def feuilles_paires(A):
    res = []
    if est_feuille(A):
        if A % 2 == 0:
            res.append(A)
    else:
        res += (feuilles_paires(fg(A)))
        res += (feuilles_paires(fd(A)))
    return res

#print(feuilles_paires(A1))

def feuilles_paires(A):
    if est_feuille(A):
        if A % 2 == 0:
            return [A]
        else:
            return []
    else:
        g = feuilles_paires(fg(A))
        d = feuilles_paires(fd(A))
    return g+d

def liste_profondeur(A, n):
    if n == 0:
        return list(racine(A))
    else:
        g = liste_profondeur(fg(A), n-1)
        d = liste_profondeur(fd(A), n-1)
    return g + d
        

#print(liste_profondeur(A1, 1))
def profondeur_max_paire(A):
    if est_feuille(A):
        if A % 2 != 0:
            return 1
        else:
            return None
    else:
        g = profondeur_max_paire(fg(A))
        d = profondeur_max_paire(fd(A))
    
        if g == None and d == None:
            return None
        elif g == None:
            return d+1
        elif d == None:
            return g + 1
        return max(1+g, 1+d)  

#print(profondeur_max_paire(A1))
A1 = arbre('+', arbre('*', 1, 4), arbre('/', arbre('+', 1, 1), 42))

def compter(A, op):
    if est_feuille(A):
        return 0
    else:
        g = compter(fg(A), op)
        d = compter(fd(A), op)
        if racine(A) == op:
            return g+d+1
        else:
            return g + d

print(compter(A1, '+'))