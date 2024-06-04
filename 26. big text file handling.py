# this program gives you the nearest number of your phone number

import math
f=open('phone_number.txt','r')

s='0'
x=0
diff=100000
p=9434644375
while(s!=''):
    s=f.readline()
    if s!='':
        n=int(s)
        if diff>abs(n-p):
            k=n
            diff=abs(n-p)
        if n==p:
            print('your number found')
            x=1
if x==0:
    print('your number not found')
print('nearest phone no of yours is',k)