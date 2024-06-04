import random
from sys import flags

l=[]
for i in range(100):
    l.append(random.randint(1,10000000))
a=int(input("Enter a number: "))

while a!=-1:
    f=0
    for i in range(len(l)):
        if a==l[i]:
            print('Found')
            f=1
            break
    if f==0:
        print("Not found")
    a=int(input("Enter a number, type -1 to exit: "))