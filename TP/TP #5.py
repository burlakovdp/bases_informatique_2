import random as r
#ex.1

def compare_et_échange(L,i):
    if L[i] > L[i+1]:
        L[i], L[i+1] = L[i+1], L[i]
        return True
    return False
#L = [3,4,5,1]
#compare_et_échange(L,0)
#assert(L) == [3, 4, 5, 1]
#compare_et_échange(L,2)
#assert(L) == [3, 4, 1, 5]

def passe_tri_bulles(L,k):
    flag = False
    for i in range(len(L)-k):
        flag = compare_et_échange(L,i) or flag
    return flag

def tri_bulles(L):
    for i in range(1, len(L)):
        flag = passe_tri_bulles(L,i)
        if i == 1 and not flag:
            #print('ICI')
            break
            

for i in range(10):
    test = []
    for j in range(10):
        test.append(r.randint(0, 10))
    #print(test, end=" ")
    tri_bulles(test)
    #print(test)
    assert(test) == sorted(test)    

#Ex.2

def fusion(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    elif L1[0] < L2[0]:
        return [L1[0]] + fusion(L1[1:], L2)
    else:
        return [L2[0]] + fusion(L1, L2[1:])

def tri_fusion(L):
    if len(L) < 2:
        return L
    else:
        L1 = tri_fusion(L[:len(L)//2])
        L2 = tri_fusion(L[len(L)//2:])
        #print(L1, L2)
        return fusion(L1, L2)
        

for i in range(100):
    test = []
    for j in range(10):
        test.append(r.randint(0, 10))
    #print(test, end=" ")
    test = tri_fusion(test)
    #print(test)
    assert(test) == sorted(test) 


#Ex.3

#print(tri_fusion([5, 1, 3, 4, 2]))

def liste_nombre_occurrences(L):
    res = [0]*(max(L)+1)
    for i in range(len(L)):
        res[L[i]] += 1
    return res

def crée_liste_triée(N):
    res = [i for i in range(len(N)) for j in range(N[i])]
    return res

def tri_comptage(L):
    return crée_liste_triée(liste_nombre_occurrences(L))

for i in range(10):
    test = []
    for j in range(100):
        test.append(r.randint(0, 100000))
    #print(test, end=" ")
    assert(tri_comptage(test)) == sorted(test)  

#Ex.4

def tri_hollandais(L):
    b = 0
    i = 0
    r = len(L)
    while i < r:
        if L[i] == 'B':
            L[i], L[b] = L[b], L[i]
            b += 1
            i += 1
        elif L[i] == 'R':
            L[i], L[r-1] = L[r-1], L[i]
            r -= 1
        elif L[i] == 'W':
            i += 1
"""
test = ['B', 'W', 'W', 'B', 'R', 'W', 'W', 'R', 'W', 'B']
tri_hollandais(test)
print(test)


for j in range(100):
    test = ["BRW"[r.randint(0,2)] for i in range(10)]
    #print(test, end=' ')
    tri_hollandais(test)
    if test != sorted(test):
        print(f'{test} != {sorted(test)}')
"""