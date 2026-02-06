#Ex.1

def u(n):
    if n == 0:
        return 234
    else:
        return 2/3*u(n-1) + 1/2

#print(u(37))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

assert(fact(3)) == 6
assert(fact(0)) == 1

def somme_cube(n):
    if n == 1:
        return 1
    else:
        return n**3 + somme_cube(n-1)

assert(somme_cube(1)) == 1
assert(somme_cube(2)) == 9
assert(somme_cube(3)) == 36
#Ex.2

def le(n):
    if n // 2 == 1 or n//2 == 0:
        return 1
    else:
        return 1 + le(n//2)
assert(le(0)) == 1
assert(le(7)) == 2
assert(le(6)) == 2
assert(le(1)) == 1
assert(le(3)) == 1
assert(le(5)) == 2
assert(le(11)) == 3

#Ex.3

def expo_rapid(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        n = b//2
        return expo_rapid(a, n)**2
    else:
        n = b//2
        return a * expo_rapid(a, n)**2

assert(expo_rapid(2,3)) == 8
assert(expo_rapid(3,2)) == 9
assert(expo_rapid(4, 4)) == 256

for i in range(10):
    for j in range(10):
        assert(expo_rapid(i, j)) == i**j
        
#Ex.4
def affiche_et_calcule_pgcd_naif(n,m):
    #print(f'calcule le pgcd de n= {n} et m={m}')
    if n == m:
        return n
    elif n < m:
        return affiche_et_calcule_pgcd_naif(m, n)
    return affiche_et_calcule_pgcd_naif(n-m,m)

d = affiche_et_calcule_pgcd_naif(21,15)

#print('Le PGCD de 21 et 15 vaut', d)

def affiche_et_calcule_pgcd(n,m):
    if n == m:
        return n
    elif n < m:
        n, m = m, n
    #print(f'calcule le pgcd de n= {n} et m={m}')
    return affiche_et_calcule_pgcd(n-m,m)

e = affiche_et_calcule_pgcd(21,15)
#print('Le PGCD de 21 et 15 vaut', e)

#Ex.6

def recherche_aux(x, tableau, a, b):
    if a >= b:
        return -1
    i = (b+a)//2
    m = tableau[i]
    if m == x:
        return i
    elif x > m:
        #print(f'1 a = {a}, b = {b}')
        return recherche_aux(x, tableau, i+1, b)
    elif x < m:
        #print(f'2 a = {a}, b = {b}')
        return recherche_aux(x, tableau, a, i)
    
def recherche(x, tableau):
    return recherche_aux(x, tableau, 0, len(tableau))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, len(a)+1):
    assert(recherche(i, a)) == i-1

for i in range(12, 1000):
    assert(recherche(i, a)) == -1
    
#Ex.7

def affiche_calcul_binaire(n):
    if n == 1 or n == 0:
        return n
    print(f'{n%2} car {n} = 2 x {n//2} + {n%2}')
    return affiche_calcul_binaire(n//2)

affiche_calcul_binaire(13)

def affiche_binaire(n):
    if n == 1 or n == 0:
        return str(n)
    return affiche_binaire(n//2) + str(n%2)

assert(affiche_binaire(1324)) == '10100101100'
