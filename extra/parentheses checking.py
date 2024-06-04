def balanced(w):
    l=[]
    x=-1
    if w=='':
        return True

    for i in range(len(w)):
        if w[i]=='(' or w[i]=='{' or w[i]=='[':
            x+=1
            l.append(w[i])
        elif (w[i]==')' or w[i]=='}' or w[i]==']') and len(l)==0:
            return False
        elif w[i]==')' and l[x]=='(':
            l.pop(x)
            x-=1
        elif w[i]=='}' and l[x]=='{':
            l.pop(x)
            x-=1
        elif w[i]==']' and l[x]=='[':
            l.pop(x)
            x-=1
        else:
            return False
        # print(l)
    
    if len(l)==0:
        return True
    else:
        return False

print(balanced('()(((())()))(())()))()'))