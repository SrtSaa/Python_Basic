'''
# factorial

n=int(input())
mul=1
if n>=0:
    while n>1:
        mul*=n
        n-=1
    print(mul)
else:
    print('Enter positive number')
'''



'''
# no of digits in a given number
  
n=abs(int(input()))
count=1
n//=10
while n>0 :
    count+=1
    n//=10
print(count)
'''



'''
# Reverse a number

x=int(input())
n=abs(x)
rev=0
while n>0:
    rev = rev*10 + (n%10)
    n//=10
if x>=0:
    print(rev)
else:
    print(rev-2*rev)
'''



'''
# Palindrome

x=abs(int(input()))
n=x
rev=0
while n>0:
    rev = rev*10 + (n%10)
    n//=10
if(x==rev):
    print('Palindrome')
else:
    print('Not a palindrome')
'''