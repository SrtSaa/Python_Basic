#taking inputs in different manner
a, b=2,3
print(a, b)
a,b=b,a
print(a, b)
del a   #delete a variable
#print(a, b)        #this line will not execute as a is deleted

a, b, c, d = input('\nEnter input: ')
print(a)
print(b)
print(c)
print(d)


print('\n')
print('alpha' in 'variable store alpha-numeric character')
print('alpha' in 'variable store numeric character')
#this is bool type and it finds given word in the given sentence


print('\n')
#operator
x=5
print('1,',1<x<9)
print('2,',10<x<20)
print('3,',x<10<x*10<100)
print('4,',x<10<x*10<10)
print('5,',10>x<=9)
print('6,',5==x>4)