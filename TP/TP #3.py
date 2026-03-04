from abe import *

#ex.1
def intérieur(ch):
    return ch[1:len(ch)-1]

def suivant(ch):
    return ch[1:]

def découpage(ch, i):
    return (ch[:i], ch[i], ch[i+1:])

#ex.2
def suppression_espaces(ch):
    res = ''
    for e in ch:
        if e != ' ':
            res += e
    return res

def remplacement_négatif(ch):
    res = ''
    tmp = 0
    signe = '(+-*/^<=>&|~'
    if ch[0] == '-':
        res += '_'
        tmp = 1
    for i in range(tmp, len(ch)):
        if ch[i] == '-':
            if res[-1] in signe:
                res += '_'
            else:
                res += ch[i]
        else:
            res += ch[i]

    return res

#ex.3
SIGNE = {'+':')))+(((', '-':')))-(((', '*':'))*((', '/':'))/((', '^':')^(', '(':'((((', ')':'))))'}

#ex.4

def parenthesage(formule):
    tmp = '(' + formule + ')'
    tmp = suppression_espaces(tmp)
    tmp = remplacement_négatif(tmp)
    res = ''
    for i in range(len(tmp)):
        if tmp[i] in SIGNE:
            res += SIGNE[tmp[i]]
        else:
            res += tmp[i]
    return res

#ex.5
nos_signes = "+-*/^<=>|&~"

def indice_racine(chaîne):
    niveau = 0
    for i in range(len(chaîne)-1, 1, -1):
        if chaîne[i] == ")":
            niveau += 1
        elif chaîne[i] == "(":
            niveau -= 1
        elif chaîne[i] in nos_signes and niveau == 0:
            return i
    return None

def decoupage_formule(chaîne):
    i = indice_racine(chaîne)
    if i == None:
        return None
    return (chaîne[:i], chaîne[i], chaîne[i+1:])

#ex.6


#ex.7
def est_arithmétique(A):
    if est_feuille(A):
        if type(A) == int:
            return True
        return False
    else:
        g = est_arithmétique(fg(A))
        d = est_arithmétique(fd(A))
        if g == False or d == False:
            return False
        return True
    
def calculer_arbre(A):
    if est_arithmétique(A):
        if est_feuille(A):
            return A
        else:
            g = calculer_arbre(fg(A))
            d = calculer_arbre(fd(A))
            if racine(A) == '+':
                return g + d
            elif racine(A) == '-':
                return g - d
            elif racine(A) == '*':
                return g * d
            elif racine(A) == '/':
                return g / d
    else:
        raise(ValueError)

def évaluer(chaîne):
    pass