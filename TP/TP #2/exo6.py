from pile import *
from abe import *

test = [1, 2, '-', 3, 4, '+', '*']


def arboriser(npi):
    signe = ['+', '-', '*', '/']
    tmp = nouvelle_pile()
    for e in npi:
        if e in signe:
            b = depile(tmp)
            a = depile(tmp)
            empile(tmp, arbre(e, a, b))
        else:
            empile(tmp, e)
    return sommet(tmp)

def calcul_direct(npi):
    signe = ['+', '-', '*', '/']
    tmp = nouvelle_pile()
    for i in range(len(npi)):
        if npi[i] in signe:
            if i == len(npi)-1:
                a = depile(tmp)
                b = depile(tmp)
                if a not in signe and b not in signe:
                    if npi[i] == '-':
                        return b-a
                    elif npi[i] == '+':
                        return a+b
                    elif npi[i] == '*':
                        return a*b
                    elif npi[i] == '/':
                        return b/a
            else:
                a = depile(tmp)
                b = depile(tmp)
                if a not in signe and b not in signe:
                    if npi[i] == '-':
                        empile(tmp, b-a)
                    elif npi[i] == '+':
                        empile(tmp, a+b)
                    elif npi[i] == '*':
                        empile(tmp, a*b)
                    elif npi[i] == '/':
                        return b/a
                else:
                    empile(tmp, b)
                    empile(tmp, a)
                    empile(tmp, npi[i]) 
        else:
            empile(tmp, npi[i])
    return sommet(tmp)

def calcul_chaîne(liste):
    signe = ['+', '-', '*', '/']
    tmp = nouvelle_pile()
    tmp_int = ''
    for i in range(len(liste)):
        if liste[i] == ' ':
            if tmp_int != '':
                empile(tmp, int(tmp_int))
                tmp_int = ''
            else:
                pass
        elif liste[i] in signe:
            b = depile(tmp)
            a = depile(tmp)
            if liste[i] == '-':
                empile(tmp, a-b)
            elif liste[i] == '+':
                empile(tmp, a+b)
            elif liste[i] == '*':
                empile(tmp, a*b)
            elif liste[i] == '/':
               empile(tmp, a/b)
        else:
            tmp_int += liste[i]
    if est_vide(tmp):
        return int(tmp_int)
    return sommet(tmp)