# Problem:

# You have n gold coins with you. 
# You wish to divide this among three of your friends under the following conditions:
# (1) All three of them should get a non-zero share.
# (2) No two of them should get the same number of coins.
# (3) You should not have any coins with you at the end of this sharing process.
# The input has four lines. The first line contains the number of coins with you. 
# The next three lines will have the share given to your three friends. 
# All inputs shall be non-negative integers. 
# If the division satisfies these conditions, then print the string FAIR. If not, print UNFAIR.



# Solution:

n=int(input())
a=int(input())
b=int(input())
c=int(input())
if a==0 or b==0 or c==0:
    print('UNFAIR')
elif a==b or a==c or b==c:
    print('UNFAIR')
elif n-(a+b+c)!=0:
    print('UNFAIR')
else:
    print('FAIR')
