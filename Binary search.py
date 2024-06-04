import re
import time

def obvious_search(l,n):
    for x in l:
        if n==x:
            return 1
    return 0

def binary_search(l,n,b,e):
    if e==b:
        if n==l[e]:
            return 1
        return 0
    else:
        mid=(b+e)//2
        if n==l[mid]:
            return 1
        elif n<mid:
            return binary_search(l,n,b,mid-1)
        else:
            return binary_search(l,n,mid+1,e)

def b_search(l,n):      #without recursion
    b=0
    e=len(l)-1
    while e-b>1:
        mid=(b+e)//2
        if n==l[mid]:
            return 1
        elif n<mid:
            e=mid-1
        else:
            b=mid+1
    if n==l[b] or n==l[e]:
        return 1
    else:
        return 0

l=list(range(10))
print(l)


a=time.time()
print(binary_search(l,9999999,0,len(l)-1))
b=time.time()
print(b-a)

a=time.time()
print(obvious_search(l,9999999))
b=time.time()
print(b-a)

a=time.time()
print(b_search(l,0))
b=time.time()
print(b-a)