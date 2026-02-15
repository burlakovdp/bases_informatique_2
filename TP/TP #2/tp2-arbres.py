from abe import *
#Ex.2
#A1 = arbre('+', arbre('*', 1, 1), arbre('/', arbre('+', 3, 1), 2))

#Ex.3

def contient42(A):
    if est_feuille(A):
        if A == 42:
            return True
        else:
            return False
    else:
        a = contient42(fg(A))
        b = contient42(fd(A))

    if a == True or b == True:
        return True
    return False
    
def compte_paire(A):
    a = 0
    b = 0
    if est_feuille(A):
        if A % 2 == 0:
            return 1
        else:
            return 0
    else:
        a += compte_paire(fg(A))
        b += compte_paire(fd(A))

    return a+b

def feuilles_paires(A):
    res = []
    if est_feuille(A):
        if A % 2 == 0:
            res.append(A)
    else:
        res += feuilles_paires(fg(A))
        res += feuilles_paires(fd(A))
    return res
        
def liste_profondeur(A, n):
    res = []
    if n == 0:
        res += racine(A)
        return res
    else:
        res += liste_profondeur(fg(A), n-1)
        res += liste_profondeur(fd(A), n-1)
    return res

A1 = arbre('+', arbre('*', 1, 1), arbre('/', arbre('+', 2, 1), 1))

def profondeur_max_pairs(A):
    a = 1
    b = 1
    if est_feuille(A):
        if A % 2 == 0:
            return 0
        else:
            return None
    else:
        tmp = profondeur_max_pairs(fg(A))
        if tmp == None:
            a = None
        else:
            a += tmp
        tmp = profondeur_max_pairs(fd(A))
        if tmp == None:
            b = None
        else:
            b += tmp
    if a == None and b == None:
        return None
    elif a == None:
        return b
    elif b == None:
        return a
    return max(a, b)

