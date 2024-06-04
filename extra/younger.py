# Problem:

# dates of birth of two persons are given. Your task is to find the younger of the two. 
# If both of them share the same date of birth, 
# then the younger of the two is assumed to be that person whose name comes first in alphabetical order.

# The input will have four lines. The first two lines correspond to the first person, 
# while the last two lines correspond to the second person. 
# For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. 
# Your output should be the name of the younger of the two.


# Solution:

a=input()
b=input()
c=input()
d=input()
x=int(b[6:10])
y=int(d[6:10])

if(x!=y):
    if(x<y):
        print(c)
    else:
        print(a)
else:
    x=int(b[3:5])
    y=int(d[3:5])
    if(x!=y):
        if(x<y):
            print(c)
        else:
            print(a)
    else:
        x=int(b[0:2])
        y=int(d[0:2])
        if(x!=y):
            if(x<y):
                print(c)
            else:
                print(a)
        else:
            if a<c:
                print(a)
            else:
                print(c)
