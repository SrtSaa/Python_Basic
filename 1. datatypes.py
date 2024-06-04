## PRINT ###

print("Enter your name:")
s=str(input())
print('Hi',s+', hope you are well.')

s=str(input('Enter your name: '))
print('Hi',s+', hope you are well.')



## DATA TYPES ###

# float, int
r=float(input('Enter the radius: '))
area=3.14*r*r
print('the area of circle of radius',r,'is',area)
print(type(area))

#list
l=[10,30.2,39,587]
print(l)
print(l[2])
print(type(l))
print(type(l[2]))
print(type(l[1]))

#bool
b1=True
b2=False
print(type(b1))
print(type(b2))
a=bool(10)
b=bool(0)
c=bool(-10)
print(a, type(a))
print(b, type(b))
print(c, type(c))
a=bool(10.2)
b=bool(0)
c=bool(-10.5)
d=bool(0.01)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
a=bool('India')
b=bool('0')
c=bool('-10.5')
d=bool('0.01')
e=bool('')            # only where string gives false value
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

#type casting
a=int(5.7)
b=int('29')
c=float(9)
d=float('45')
e=str(5)
f=str(5.6)
# g=int('n')       # not possible
# h=int('nine')    # not possible
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
# print(g, type(g))
# print(h, type(h))