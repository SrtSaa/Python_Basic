'''
for x in range(10):
    print(x)

print('\n')

for x in range(10):
    print(x,end=' ')
'''



'''
d=15
m=5
y=2022
print("1. Today's date is",d,m,y)
# we can see there is a space between each variable
# this is caused whenever a comma(,) is used
# because print statement has another parameter named 'sep'(i.e. seperater)
# the default value of sep is one space
# whenever a comma is used sep is executed

print("\n2. Today's date is",d,m,y,sep='/')
# now there is a / between is and date 
# because a comma used between them

print("\n3. Today's date is", end=' ')
print(d,m,y,sep='/')

print("\n4. Today's date is", end=' ')
print(d,m,y,sep='-')
'''



'''
n=int(input())
for i in range(1,11):
    #print(n,'X',i,'=',n*i)      #here use 5 var(3 int, 2 string) in a single print statement

    #print(f'{n} X {i} = {n*i}')
    # here only one string is used inside the print statement where we use integers inside it
    # here f stands for formatted print

    #print('{0} X {1} = {2}'.format(n,i,n*1))
    # here 0 represents n, 1 represents i, 2 represents n*i

    print('%d X %d = %d' %(n,i,n*i))
    # this method is known as print using string modulo operetor
'''




pi=22/7
print(f'value of pi = {pi}')
print('value of pi = {0}'.format(pi))
print('value of pi = %f' %(pi))

print(f'value of pi = {pi:.3f}')
print('value of pi = {0:.5}'.format(pi))
print('value of pi = %.5f' %(pi))