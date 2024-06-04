'''
Problem:

Accept a positive integer n as input and find all solutions to the equation:
x^2 + y^2 = z^2
subject to the following constraints:
(1) x, y and z are positive integers
(2) x < y < z < n

Print each solution triplet on one line — x,y,z — with a comma between consecutive integers. 
The triplets should be printed in ascending order. 
If you do not find any solutions satisfying the given constraints,
print the string NO SOLUTION as output.
'''


# Sollution:
n=int(input())
f=0
for i in range(1,n-1):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i**2+j**2==k**2:
                print(i,j,k,sep=',')
                f=1
if f==0:
    print('NO SOLUTION')
