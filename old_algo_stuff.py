import random
import itertools
# insertion sort(non-decreasing)
def insertion_sort(A):
    j = 1
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

#print insertion_sort([5,2,4,6,1,3]), "\n"
#print insertion_sort([31,41,59,26,41,58]), "\n"

# descending insertion sort(non-decreasing)
def desc_insertion_sort(A):
    j = 1
    for j in range(len(A)):
        key = A[j]
        i = j -1
        while i > -1 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

#print desc_insertion_sort([5,2,4,6,1,3]), "\n"
#print desc_insertion_sort([31,41,59,26,41,58]), "\n"

# linear search algorithm
def linear_search(A,v):
   for i in range(len(A)):
       if A[i] == v:
           return i
       elif A[i] != v and i == len(A)-1:
           return "NIL"


#print linear_search([5,2,4,6,1,3,31,41,59,26,41,58],100)

# merge sort, divide and conqure algorithm
def merge_step(a,b):
    c = []
    print "(before while) a = ",a, "\n"
    print "(before while) b = ", b, "\n"
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c
def mergesort(x):
    print " before (if, else) x = " , x, "\n"
    print " the length of x = ", len(x), "\n"
    if len(x) == 0 or len(x) == 1:
       # print "in if x = ", x, "\n"
        return x
    else:
        midpoint = len(x)/2
        a = mergesort(x[:midpoint])
        #print  " (after a) x = ", x, "\n"
        b = mergesort(x[midpoint:])
        #print  " (after b) x = ", x, "\n"
        return merge_step(a,b)

#print mergesort([4,3,1,2]), "\n"



""" Strassen's Algorithm for Square Matrix Multiplication"""

def Matrix_Mult(A, B):

    n = len(A)
    C = [[] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            HOLD = 0
            for k in range(len(B)):
                HOLD += A[i][k]*B[k][j]
            C[i].append(HOLD)

    return C

#print Matrix_Mult(A = [[1,2],[3,4]], B = [[1,2],[3,4]])

""" Devide and Conquer Square Matrix Multiplication """

""" Combinatorics algorithm """

def cmbn_r(n,r):
    m = n-r
    if m == 1:
        return 1
    else:
        return m*cmbn_r(n-1,r)


print cmbn_r(7,3)


