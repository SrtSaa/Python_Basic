a = [42]
b = [1,2,3,4,5]
c = [[1,2,3],[4,5,6]]
d = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]

print(a)
print(b)
print(c)
print(d)

print()
print()


import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a,a.ndim,'\n')
print(b,b.ndim,'\n')
print(c,c.ndim,'\n')
print(d,d.ndim,'\n')

