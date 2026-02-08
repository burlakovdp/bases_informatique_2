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
    if len(L) ==  2:
        return fusion(list(L[0]), list(L[1]))
    elif len(L) % 2 != 0:
        tri_fusion(L[:len(L)//2+1]) + tri_fusion(L[len(L)//2+1:])
    else:
        tri_fusion(L[:len(L)//2]) + tri_fusion(L[len(L)//2:])


        
L = [7, 6, 5, 4, 3, 2, 1, 0]
L1 = [3, 2, 1, 0]
#print(fusion([3], [2]))
print(tri_fusion(L1))

