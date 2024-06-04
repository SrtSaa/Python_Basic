import imp


import random

a=random.random()       #it gives a random number between 0 and 1
print('a= ',a)

#tossing a coin
if(a<.5):
    print('H')
else:
    print('T')


print('\n')
b=random.randrange(1,7)   #it gives an integer no between two given range excluding last one
print('b= ',b)
c=random.randint(1,6)   #it gives an integer no between two given range including last one
print('c= ',c)

#tossing two dice, and sum of its results
print('The sum of output of two dice is: ',b+c)
