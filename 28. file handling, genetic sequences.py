'''f=open('my.txt','w')
f.write('0123456789')
f.close()

f=open('my.txt','r')
print(f.read(2))
print(f.read(3))
print(f.read(1))

# .read() sequentially print from the file
# we can not back track using read command
# for this reason we use seek command
# it goes to a perfect index position

print(f.seek(2))
print(f.seek(7))
print(f.seek(1))

f.close()'''


import random
s='ATGC'

f=open('my.txt','w')
for i in range(100000000):
    r=random.randrange(0,4)
    f.write(s[r])
f.close()
