'''
a = [10, 20, 30, 40, 50]
b = [15, 10, 15, 20, 25]

sub = lambda x,y: x-y
incr = lambda x: x+1

c = map(sub,a,b)
print(list(c))

c = map(incr,a)
print(list(c))
'''



import math

a = [25, -16, 9, 81, -100]

sq = lambda x: math.sqrt(x)

def is_positive(n):
    if n>=0:
        return n

c = map(sq, filter(is_positive, a))
print(list(c))