import string
import random
import calendar

f=open('scores.csv','w')
f.write('CardNo,Name,Gender,DateOfBirth,CityTown,Mathematics,Physics,Chemistry,Total\n')

# required variables, lists
a=string.ascii_lowercase
g='FM'
m=calendar.month_abbr[1:]
c=[]
for i in range(8):
    n=''
    x=random.randrange(4,9)
    for j in range(x):
        k=random.randrange(0,26)
        n+=a[k]
    c.append(n)

for i in range(30):

    # inserting index no.
    f.write(str(i))
    f.write(',')

    # inserting name
    x=random.randrange(4,11)
    n=','
    for j in range(x):
        k=random.randrange(0,26)
        n=a[k]+n
    f.write(n)

    # inserting gender
    x=random.randrange(0,2)
    f.write(g[x])
    f.write(',')

    # inserting DOB
    x=random.randrange(0,12)
    d=' '+m[x]+','
    if d==' Feb,':
        x=random.randrange(1,29)
    else:
        x=random.randrange(1,29)
    d=str(x)+d
    f.write(d)

    # inserting city
    x=random.randrange(0,len(c))
    f.write(c[x])
    f.write(',')

    # inserting marks
    total=0
    for i in range(3):
        x=random.randrange(40,101)
        f.write(str(x))
        f.write(',')
        total+=x
    f.write(str(total))

    f.write('\n')


f.close()