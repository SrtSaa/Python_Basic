# set in python is a data structure that represents a group of numbers.
# in set repeatation of a number is not allowed.
# if there is any repeatation it removes it.
# it prints data in sorted order


import sys


y={2,5,1,7,2,12,5}
type(y)
print(y)
print(2 in y)
print(-1 in y)


# differnces between set and list are:
# i> searching a particular data in a large set is much faster than that of list
# ii> size of set is more than size of list for same value
# iii> set is not subscriptable

l=list(range(10000000))
s=set(range(10000000))

# i
print(9999999 in s)
print(9999999 in l)

# ii
print(sys.getsizeof(l))
print(sys.getsizeof(s))

# iii
print(l[0])
# print(s[0])

s={1,2,5,4,'set'}
s.add('type')
print(s)
