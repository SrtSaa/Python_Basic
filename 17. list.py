
#M=[[1,2,3],[2,4,5],[3,5,6]]
M=[[1,2,3],[5,4,5],[3,5,6]]
sym = True
for i in range(len(M)):
    for j in range(len(M)):
        if(M[i][j] == M[j][i]):
            sym = True
        else:
            print('inside else')
            sym = False
            break
if sym:
    print('YES')
else:
    print('NO')

print(M[0][1])
print(M[1][0])