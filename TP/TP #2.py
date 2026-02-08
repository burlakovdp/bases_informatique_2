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

def fusion(L1, L2, ac = []):
    if len(L1) == 0:
        ac += L2
        return ac
    elif len(L2) == 0:
        ac += L1
        return ac
    if L1[0] < L2[0]:
        ac.append(L1[0])
        return fusion(L1[len(ac):], L2)
    elif L2[0] < L1[0]:
        ac.append(L2[0])
        return fusion(L1, L2[len(ac):])

def tri_fusion(L):
    if len(L) < 2:
        return L
    elif len(L) % 2 != 0:
        L1 = L[:len(L)//2+1]
        L2 = L[len(L)//2+1:]
    else:
        L1 = L[:len(L)//2]
        L2 = L[len(L)//2:]
        

        
L = [7, 6, 5, 4, 3, 2, 1, 0]
L1 = [5, 1, 3, 4, 2]
L2 = [4, 3]
L3 = [1]
#print(fusion([3], [2]))
#print(fusion(L2, L3))
#print(tri_fusion(L1))



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
        if i >= r:
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