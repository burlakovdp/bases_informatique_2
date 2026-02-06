#Ex.1

def insertion_sort(A,n):
    for i in range(1, n):
        key = A[i]
        j  = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -=1
        A[j+1] = key

A = [5, 4, 3, 2, 1, 0]

print(A)

insertion_sort(A, len(A))

print(A)

#Ex.2
A = [5, 4, 3, 2, 1, 0]
print(A)
def echange(A, i1, i2):
    A[i1], A[i2] = A[i2], A[i1]

def algo_2(A, n):
    elem = None
    index = None
    for j in range(n):
        elem = A[j]
        index = j
        for i in range(j, n):    
            if A[i] < elem:
                elem = A[i]
                index = i
        echange(A, index, j)

algo_2(A, len(A))
print(A)
#complex O(n**2)

#Ex.3

#1 int -> String
#2 int x int x int -> int
#3 (USE): int -> int, mistery3 int x int -> int
#4 int -> int
