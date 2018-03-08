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

print mergesort([4,3,1,2]), "\n"
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print factorial(6)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
