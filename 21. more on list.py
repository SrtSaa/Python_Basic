
l1=[1,2,3]
l2=[4,5,6]
l12=l1+l2
l21=l2+l1
print(l12)
print(l21)
print()



m=[0]*5
print(m)
l1=l1*5
print(l1)
print()



print([1,2]<[2,1])
print([1,2,4]<[1,2,3])
print([2,3]<[1])
print([]<[1])
print()
# list comparison is done element by element
# first element of the list compared with first element of another list
# if it can return true or flase then stops
# otherwise it compares second elements of both lists



# list are mutable i.e. we can change any of the element as we wish
# but tuple, string are immutable i.e. we can not change the value of any element



x=5
y=x
x=10
print(x,y)

l1=[1,2,3]
l2=l1
l1[0]=100
print(l1)
print(l2)
print()

# in l1=[1,2,3], computer takes a memory location and named as l1 and there stores the value
# in l2=l1, instead of creating new memory location computer simply adds one more name(l2) the same memory location which was named l1
 


l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()

# 'is' operator can be used to find that whether two variables have same memory location
l5=l1
print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)
print()



def add(x):
    x.append(1)
    return x

x =[5]
print(x)
print(add(x))
print(x)
# in case of list whenever we pass a list in a fuction, the original list will be effected whenever some operations are performed on it in the funcion
print()


l=[1,2,3]
l.append(0)     # it inserts an element at the end of the list
print(l)
l.insert(2,9)   # it inserts an element at the given index 
print(l)
l.remove(2)     # it deletes the given element
print(l)
l.pop(2)        # it deletes the elements which is present in the given index
print(l)
l.sort()        # it sorts the list in the ascending order
print(l)
l.reverse()     # it actually reverses the list
print(l)