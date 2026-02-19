#Ex.1
def compare_et_echanger(L, i):
    if L[i] > L[i+1]:
        L[i], L[i+1] = L[i+1], L[i]

def passe_tri_bulles(L, k):
    for i in range(len(L)-k-1):
        compare_et_echanger(L, i)

def tri_bulles(L):
    for i in range(len(L)):
        tmp = list(L)
        passe_tri_bulles(L, i)
        if tmp == L:
            break
L = [1, 2, 3]

#tri_bulles(L)
#print(L)

#Ex.2

def fusion(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    else:
        if L1[0] > L2[0]:
            return L2[:1] + fusion(L1, L2[1:])
        return L1[:1] + fusion(L1[1:], L2) 
        
def tri_fusion(L):
    if len(L) < 2:
        return L
    else:
        L1 = tri_fusion(L[:len(L)//2])
        L2 = tri_fusion(L[len(L)//2:])
        return fusion(L1, L2)
    
assert(tri_fusion([])) == []
assert(tri_fusion([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert(tri_fusion([5, 4, 3, 2, 1])) == [1, 2, 3, 4, 5]
assert(tri_fusion([4, 5, 2, 1, -1, 0, 20])) == [-1, 0, 1, 2, 4, 5, 20]

#Ex.3

def max_list(L):
    tmp = -1
    for i in range(len(L)):
        if L[i] > tmp:
            tmp = L[i]
    return tmp

def liste_nombre_occurrences(L):
    res = []
    for i in range(max_list(L)+1):
        counter = 0
        for j in range(len(L)):
            if i == L[j]:
                counter += 1
        res.append(counter)
    return res

def cree_liste_triee(N):
    res = []
    for i in range(len(N)):
        for j in range(N[i]):
            res.append(i)
    return res

def tri_comptage(L):
    return cree_liste_triee(liste_nombre_occurrences(L))


#Ex.4

def tri_hollandais(L):
    b = 0
    r = len(L)-1
    i = 0
    while True:
        if i > r:
            return
        if L[i] == 'B':
            L[b], L[i] = L[i], L[b]
            b += 1
            i += 1
        elif L[i] == 'R':
            L[r], L[i] = L[i], L[r]
            r -= 1
        elif L[i] == 'W':
            i += 1