# Problem:

# Accept two positions as input: start and end. 
# Print YES if a bishop at start can move to end in exactly one move. Print NO otherwise. 
# Note that a bishop can only move along diagonals.



#Solution:

s='ABCDEFGH'
x=input()
y=input()
d=int(x[1])-int(y[1])
if s[(s.index(x[0])+d)%8]==y[0]:
    print('YES')
elif s[(s.index(x[0])-d)%8]==y[0]:
    print('YES')
else:
    print('NO')