from abe import *
CARACTÈRES = "(+-*/^<=>&|~"
#Ex.1

def intérieur(ch):
    return ch[1:len(ch)-1]

assert(intérieur("(2+3)")) == '2+3'

def suivant(ch):
    return ch[1:]

assert(suivant("-(2+3)")) == '(2+3)'

def découpage(ch, i):
    return (ch[:i], ch[i], ch[i+1:])

assert(découpage("(2+3)*(4+5)", 5)) == ('(2+3)', '*', '(4+5)')

#Ex.2

def suppression_espaces(ch):
    res = ''
    for e in ch:
        if e != ' ':
            res += e
    return res

assert(suppression_espaces("( 2+ 3) * ( 4 + 7) ")) == '(2+3)*(4+7)'

def remplacement_négatif(ch):
    if len(ch) == 0:
        return ch
    tmp = ''
    res = ''
    if ch[0] == '-':
        tmp += '_'
    else:
        tmp += ch[0]
    for e in ch[1:]:
        tmp += e

    for i in range(len(tmp)):
        if tmp[i] == '-' and tmp[i-1] in CARACTÈRES:
            res += '_'
        else:
            res += tmp[i]
    return res

assert(remplacement_négatif("")) == ''
assert(remplacement_négatif("1+-3")) == '1+_3'
assert(remplacement_négatif("1-3")) == '1-3'
assert(remplacement_négatif("-1-3")) == '_1-3'
assert(remplacement_négatif("-(1+2)--5")) == '_(1+2)-_5'

#Ex.3
dico = {"+": ')))+(((', "-": ')))-(((', "*": '))*((', '/': '))/((', '^': ')^(', '(': '((((', ')':'))))'}

#Ex.4
def parenthèsage(formule):
    tmp = '(' + formule + ')'
    tmp = remplacement_négatif(suppression_espaces(tmp))
    res = ''
    for e in tmp:
        if e in dico:
            res += dico[e]
        else:
            res += e
    return res

assert(parenthèsage("-1+2 *3")) == '((((_1)))+(((2))*((3))))'

#Ex.5

def indice_racine(chaîne):
    niveau = 0
    for i in range(len(chaîne)-1, -1, -1):
        if chaîne[i] == ")":
            niveau += 1
        elif chaîne[i] == '(':
            niveau -= 1
        elif niveau == 0 and chaîne[i] in CARACTÈRES:
            return i
    return None 

def découpage_formule(chaîne):
    if indice_racine(chaîne) == None:
        return None
    return découpage(chaîne, indice_racine(chaîne))
    

assert(découpage_formule("1-5+2-(3*5)")) == ('1-5+2', '-', '(3*5)')
assert(découpage_formule("5")) == None

#Ex.6
nombres = '0123456789'
def arboriser_propre(ch):
    tmp = découpage_formule(ch)
    if tmp == None:
        try:
            if ch[0] in nombres:
                return int(ch)
            elif ch[0].isalpha():
                return ch
            elif ch[0] == '(':
                return arboriser_propre(intérieur(ch))
            elif ch[0] == '_':
                return arbre('-', 0, arboriser_propre(suivant(ch)))
        except:
            raise ValueError(f"formule {ch} invalide")
    elif tmp != None:
        return arbre(tmp[1], arboriser_propre(tmp[0]), arboriser_propre(tmp[2]))
    

def arboriser(ch):
    return arboriser_propre(parenthèsage(ch))

#Ex.7

def est_arithmétique(A):
    if est_feuille(A):
        return type(A) == int
    else:
        g = est_arithmétique(fg(A))
        d = est_arithmétique(fd(A))
        return g and d
    
assert(est_arithmétique(arboriser("1-x+2-(3*5)"))) == False
assert(est_arithmétique(arboriser("1-5+2-(3*5)"))) == True

def calculer_arbre(A):
    try:
        if est_feuille(A):
            return A
        else:
            g = calculer_arbre(fg(A))
            d = calculer_arbre(fd(A))
            if racine(A) == '+':
                return g+d
            elif racine(A) == '-':
                return g-d
            elif racine(A) == '/':
                return g/d
            elif racine(A) == '*':
                return g*d
            elif racine(A) == '^':
                return g**d 
    except:
        raise ValueError("arbre n'est pas arithmétique")
    
assert(calculer_arbre(arboriser("(3^5)+10"))) == 253

def évaluer(chaîne):
    return calculer_arbre(arboriser(chaîne))

"""
def repl():
    while True:
        try:
            ch=input("> ")
            if ch=="q":
                return
            try:
                est_arithmétique(ch)
            except:
                print("Wrong line")
            print(évaluer(ch))
        except:
            print("Wrong line")

if __name__ == "__main__":
    repl()
"""
#Ex.8

def variables(A):
    if est_feuille(A):
        return [A]
    else:
        g = variables(fg(A))
        d = variables(fd(A))
        return g + d
    
print(variables(arboriser("(x^5)+10")))

def évaluer_environnement(A,env):
        if est_feuille(A):
            if type(A)==str:
                    return env[A]
            else:
                return A
        else:
            g = évaluer_environnement(fg(A), env)
            d = évaluer_environnement(fd(A), env)
            if racine(A) == '+':
                return g+d
            elif racine(A) == '-':
                return g-d
            elif racine(A) == '/':
                return g/d
            elif racine(A) == '*':
                return g*d
            elif racine(A) == '^':
                return g**d 
env = {'g':12, 'y':4}
print(évaluer_environnement(arboriser("(x*5)+y"), env))