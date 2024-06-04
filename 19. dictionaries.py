d={}
print(type(d))
d['a']=43
d['v']='sd'
d['d']=[64,52,47]
print(d)
print(d['a'])
print(d['d'][1])
print("\n")

l=['o','s','s','t','f','m','s','r','t']
print(l)
s=set(l)
print(s)

d={}
for x in s:
    d[x]=0
print(d)
for x in l:
    d[x]+=1
print(d)

m=0
for x in d:
    if d[x]>m:
        m=d[x]
        word=x
print(m,word)
