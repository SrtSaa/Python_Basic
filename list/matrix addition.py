dim=3

r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[8,2,5]
s2=[9,1,7]
s3=[4,3,2]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

c=[[0,0,0],[0,0,0],[0,0,0]]
#c=[[],[],[]]       #it is not correct


for i in range(dim):
    for j in range(dim):
        c[i][j]=A[i][j]+B[i][j]

print(c)
