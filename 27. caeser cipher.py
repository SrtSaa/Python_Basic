'''caesar cipher means shift the letters ny n units'''

import string

def create_cc():
    l=string.ascii_lowercase
    l=list(l)
    d={}
    for i in range(len(l)):
        d[l[i]]=l[(i+3)%26]
    return d

def only_lower(x):
    file=open(x,'r')
    l=list(file.read())
    file.close()

    for i in range(len(l)):
        if l[i].isupper():
            l[i]=l[i].lower()

    m=[]
    for i in l:
        if i.isalpha():
            m.append(i)

    s=x[:-4]+"_converted"+x[-4:]
    file=open(s,'w')
    for i in m:
        file.write(i)
    file.close()

    return s




s=input("Enter the file name: ")
s = only_lower(s)
k=s[:-4]+"_encrypted"+s[-4:]

f=open(s,'r')
g=open(k,'w')
di=create_cc()

c=f.read(1)
while c!='':
    g.write(di[c])
    c=f.read(1)

f.close()
g.close()






