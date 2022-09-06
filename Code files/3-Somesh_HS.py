def parent (i):
    return i/2
def LEFT(i):
    return 2*i
def right(i):
    return 2*i + 1



def MAX_HEAPIFY(A,i):

    l = LEFT(i)
    r = right(i)

    if l<=len(A) - 1 and A[l] > A[i]:
        largest = l
    else: largest = i
    if l<= len(A)- 1 and A[r]>A[largest]:
        largest = r
    if largest != i :

        A[i],A[largest] = A[largest],A[i]
       # print(A)

        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP (A):
   # n = len(A)
    for i in range (len(A)//2 - 1, 1, -1 ):
      #  print(A)
        MAX_HEAPIFY(A,i)

def HEAPSORT(A):
    #n= len(A)
    BUILD_MAX_HEAP(A)
    for i in range (len(A) -1,2,-1):
        A[i],A[0] = A[0],A[i]
        #swap(A[1],A[i])
       # n = n-1
        MAX_HEAPIFY(A,i)
       # print(A)
        return A

A = [12, 11, 13, 5, 6, 7 ]
print("The original Array is: ", A)
print('The Sorted Array is:   ',HEAPSORT(A))

