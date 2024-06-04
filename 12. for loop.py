for i in range(5):     # i is starting from 0 to x (excluding)
    if(i%2==0):
        print(i)

print('\n')
n=int(input())
for i in range(n):
    print(i)

print('\n')
for i in range(3,n):        # from x(including) to y(excluding)
    print(i)

print('\n')
for i in range(3,n,2):        # from x(including) to y(excluding) jumping z steps
    print(i)