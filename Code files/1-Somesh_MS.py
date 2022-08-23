def mergingprocess(Arr,p,q,r):
    n1= q-p-1
    n2= r-q

    L = [0]*(n1); R= [0]*(n2)

    for i in range (0,n1):
        L[i] = Arr[p+i]
    for j in range (0,n2):
        R[j] = Arr[q+j+1]

    i=j=0;k=1
    while i < n1 and j < n2:

        if L[i] <= R[j]: #Originlly, at this line i was getting index out of bound error so tried with while loop, and added code for copying remaining elements in the array .
            Arr[k] = L[i]
            i =i+1
        else: Arr[k]=R[j] ; j =j+1
        k =k+1

    while i<n1:
        Arr[k] = L[i]
        i= i+1
        k=k+1
    while j <n2:
        Arr[k] = R[j]
        j=j+1

def Sortprocess(Arr, p, r):
    if p < r:
        q= (p+r)//2
        Sortprocess(Arr, p, q)
        Sortprocess(Arr, q + 1, r)
        mergingprocess(Arr, p, q, r)


Arr = [12, 11, 13, 5, 6, 7]
n = len(Arr)
print("Given array is: ",Arr)
Sortprocess(Arr, 0, n-1)
print("Sorted array is: ", Arr)


