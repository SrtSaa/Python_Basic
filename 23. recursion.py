# check 0 is present in the list
'''
def check0(l):
    if len(l)==0:
        return 0
    if l[0]==0:
        return 1
    else:
        return check0(l[1:len(l)])
 
print(check0([1,5,8,2,8]))

'''

# sorting

def mini(l):
    m=l[0]
    for x in l:
        if x<m:
            m=x
    return m

def sort(l):
    if l==[] or len(l)==1 :
        return l
    m=mini(l)
    l.remove(m)
    return [m]+sort(l)

l=[2,8,1,6,8,7,2,4,6,2,64]
print(sort(l))
