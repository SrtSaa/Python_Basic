from itertools import count


s='VIBGYOR'
t='VIBGYOR'

count=0
for i in range(7):
    for j in range(7):
        print(s[i], s[j])
        #print(s[i], s[j], sep='')
        count+=1

print(count)

