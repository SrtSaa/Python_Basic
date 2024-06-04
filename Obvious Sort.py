l=[12,5,52,1,36,42,6,24,51,5,454,25,14,1,2]
x=[]

while len(l)>0:
    min=l[0]
    for i in range(len(l)):
        if l[i]<min:
            min = l[i]
    x.append(min)
    l.remove(min)
    
print(l)
print(x)