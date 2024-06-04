l=list(input().split(' '))
s=set(l)
n=3
d={}
for x in s:
    d[x]=0
for x in l:
    d[x]+=1
for x in d:
    if d[x]==n:
        print('ok')
        #return true
print('not')
#return false