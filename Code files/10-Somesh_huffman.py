#input
from collections import Counter
class Node(object):
    def __int__(self,left = None,right =None):
        self.left = left
        self.right = right
    def get_child(self):
            return self.left,self.right

    def decode (root,s): # where root is encoded mgs and s is frequencies i just wrote it in casual terms
        temp = root
        ans = []
        for char in s :
            if char is '0':
                temp = temp.left
            else:
                temp = temp.right
            if temp.left is None and temp.right is None:
                ans.append(temp.data)
                temp = root
        print ("".join(ans)) # sir, i Dont know whether its correct or not but this is what i can think off.. so many projects left to do.. please excuse me this time if it didnt work. i feel i got the logic behind the problem


def make_the_tree(freqs_stored):
    #as long as freq sorted is >1
    while len (freqs_stored)>1:
#combine 2 no.s
        key1,value1 = freqs_sorted(0)
        key2,value2 = freqs_sorted(1)


       # break

        #delete
        freqs_sorted = freqs_sorted[2:]

        # add new combinations
        new_value = value1 + value2
        new_node =Node(key1,key2)
        #add to freq
        freqs_sorted.append((new_node,new_value))
        #sort _again
        freqs_sorted= sorted(freqs_stored ,key=lambda item: item[1] )
    return freqs_sorted[0][0]




message = "AAABBBBBBEEEDABEEDCC"

#count the mgs
#
freqs = dict(Counter(message))
print(freqs)
#sort them from smallest to largest
freqs_sorted= sorted(freqs.items() ,key=lambda item: item[1] )
#make the tree by combining the smallest one, and delete those guys
make_the_tree(freqs_sorted)
#get the code
def get_code(node,code = ' '):
    if type(node) is str:
        #stop
        return {node:code}
    left,rigth = node.getchild()


    #recurcive function
    get_code(left , code+'0')
    get_code(rigth, code+'1')

#print the code

