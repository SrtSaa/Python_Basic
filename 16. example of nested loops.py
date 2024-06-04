
'''
# find all prime numbers less than the entered number

n=int(input())
if n>2:
    print('2',end=' ')
    for i in range(3,n):
        f=0
        for j in range(2,i):
            if i%j==0:
                f=1
                break
        if f==0:
            print(i,end=' ')
'''


'''
# find the daywise total rainfall for the entered duration of time

n=int(input())
for i in range(1,n+1):
    r=0
    x=int(input())
    while x!=-1:
        r+=x
        x=int(input())
    print(f'day {i} total rainfall is: {r}')
'''




# Find the length of longest word from the set of sentences entered

s=input()
max=0
while s!='-1':
    count=0
    # for i in range(len(s)):
    #     if s[i]==' ':
    for i in s:
        if i==' ':
            if count>max:
                max=count
            count=0
        else:
            count+=1
    s=input()
print(max)
