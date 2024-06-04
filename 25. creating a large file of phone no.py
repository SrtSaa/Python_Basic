import random as r

f=open('phone_number2.txt','w')
for i in range(10):
    s=str(r.randrange(6,10))
    for i in range(9):
        s+=str(r.randrange(0,10))
    f.write(s)
    f.write('\n')
f.close()

