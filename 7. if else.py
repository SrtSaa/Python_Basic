
'''
#age checking
#age must be 13 to watch the movie

cy=2022
by=int(input("Enter your year of birth: "))
age=cy-by
if(age<13):
    print('you are not old enough')
    print('sorry, you cannot watch this movie')
else:
    print('you\'re old enough to see this movie')
    print('don\'t forget watch prequels')
print('Have a nice day')
'''


'''
#even or odd

a=int(input())
if(a%2==0):
    print('even')
else:
    print('odd')
'''


'''
#chech number is ends with 0 or 5

a=int(input())
if(a%5==0):
    if(a%10==0):
        print(0)
    else:
        print(5)
else:
    print('other')
'''

'''
#grade a student based on marks

a=float(input())
if(0<=a<=100):
    if(a>=90):
        print('A')
    elif(a>=80):
        print('B')
    elif(a>=70):
        print('C')
    elif(a>=60):
        print('D')
    else:
        print('E')
else:
    print('invalid input')
'''


'''
#implimentaion of flowchart:

                                  TIME
                                   |
                                   v
               --------longer---------------shorter--------
               |                                          |
               v                                          v
             PRICE                                      PRICE
               |                                          |
  ---lower-----------higher---              ---lower-----------higher---
  |                          |              |                          |
  v                          v              v                          v
coach                      train       red eye flight            daylight flight


l=int(input('define longer for time: '))
h=int(input('define higher for price: '))

t=int(input('enter time: '))
if(t>=l):
    p=int(input('enter price: '))
    if(p>=h):
        print('train')
    else:
        print('coach')
else:
    p=int(input('enter price: '))
    if(p>=h):
        print('red eye flight')
    else:
        print('daytime flight')
'''