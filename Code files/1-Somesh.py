#Arr = [5,2,4,3,1,6]
Arr = []
n = int(input("Enter the count for your array & then press enter followed by numbers ="))
for i in range(0, n):
    addo = int(input())
    Arr.append(addo)
print("Unsorted array :",Arr)
for j in range(1, len(Arr)):
    key = Arr[j]
    i = j - 1
    while i >= 0 and Arr[i] > key:
        Arr[i + 1] = Arr[i]
        i = i - 1
    Arr[i + 1] = key

#print("key = ", key)
print("Sorted :",Arr)








################################################################
#other way to do
# for i in range(0,len(Arr)-1):
#     for j in reversed(range (i+1, i>0)):
#         if Arr[j]< Arr[j-1] :
#             temp = Arr[j]
#             Arr[j] = Arr[j-1]
#             Arr[j-1] = temp
#             print(Arr)
#             #print(temp)
#         else: break
#

