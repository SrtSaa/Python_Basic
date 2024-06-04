'''
# Problem:

Accept a positive integer n as input and print a "number arrow" of size n.

For example, n = 5 
output:
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
'''


# Solution
n=int(input())

for i in range(1,2*n):
    for j in range(1,n-abs(n-i)+1):
        print(j,end='')
        if j<n-abs(n-i):
            print(',',end='')
    print()s