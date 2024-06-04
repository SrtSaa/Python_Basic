import random

l=[]

for i in range(30):
    #l.append(random.random())
    l.append(random.randint(1,365))

l.sort()
print(l)

i=0
f=0
while(i<len(l)-1):
    if l[i]==l[i+1]:
        print('repeats',l[i])
        f=1
    i+=1
if(f==0):
    print('does not repeat')