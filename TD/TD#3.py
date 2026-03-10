def countSort(A):
    C = [0]*len(A)
    for j in range(len(A)):
        C[A[j] ] += 1
    g = 0
    for i in range(len(C)):
        while C[i] > 0:
            A[g] = i
            C[i] -= 1
            g += 1
            
    
a = [3, 0, 2 ,1, 1, 4, 0, 0, 0]
C = [0, 1, 2, 1, 1]
print(a)
countSort(a)
print(a)