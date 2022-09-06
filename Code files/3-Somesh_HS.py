def parent (i):
    return i/2
def LEFT(i):
    return 2*i
def right(i):
    return 2*i + 1



def MAX_HEAPIFY(A,n,i):
    largest = i
    l = LEFT(i)
    r = right(i)

    if l< n and A[i] < A[l]:
        largest = l
    #else: largest = i
    if r< n and A[largest]<A[r]:
        largest = r
    if largest != i :
        #swap(A[i],A[largest])
        A[i],A[largest] = A[largest],A[i]

        MAX_HEAPIFY(A,n,largest)

def BUILD_MAX_HEAP (A):
    n = len(A)
    for i in range (n//2 , -1, -1 ):
        MAX_HEAPIFY(A,n,i)

def HEAPSORT(A):
    n= len(A)
    BUILD_MAX_HEAP(A)
    for i in range (n - 1,0,-1):
        A[i],A[0] = A[0],A[i]



        MAX_HEAPIFY(A,i,0)
    return A

A = [12, 11, 13, 5, 6, 7 ]
print("The original Array is: ", A)
#n= len(A)
#ANS=HEAPSORT(A)
print('The Sorted Array is:   ',HEAPSORT(A))
# it took me long time to find ou the problem sir i made some changes accordingly. It fun altogether 
