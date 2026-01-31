#Ex.1

def compare_et_échange(L,i):
    if L[i] > L[i+1]:
        L[i], L[i+1] = L[i+1], L[i]
    return L

def passe_tri_bulles(L,k):
    for i in range(k):
        tmp = L
        for j in range(len(L)-1):
            L = compare_et_échange(L, j)
        
        if tmp == L:
            return L
            
    return L

def tri_bulles(L):
    for i in range(len(L)-1):
        L =  passe_tri_bulles(L,i)
    return L

