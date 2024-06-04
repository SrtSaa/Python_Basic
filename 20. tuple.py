# tuple data type is unchangeable
# whereas a list can be changable




l=[4,5,2,8,1,14,86]
l.append(0)
l.remove(5)
print(l)

t=(4,5,2,8,1,14,86)
print(t)
#t.add(5)
print("\n")



import string
x=string.ascii_letters
print(x)
print()
alpha=tuple(x)
print(alpha,"\n")
#this print does not maintain any order

alpha=tuple(list(x))
print(alpha,'\n')

m='aja;jgagj rjojfalf afkalfj;a;jalg af,mfj'
l=list(m)
r=[]
for x in l:
    if x in alpha:
        r.append(x)
print(r)
