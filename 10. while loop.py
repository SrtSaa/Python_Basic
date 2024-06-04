'''
print('When did India get its independence (year)?')
year=int(input())
while(year!=1947):
    print('wrong')
    print('enter once again.')
    year=int(input())
print('correct')
'''


'''
# break
email=input()
for c in email:
    if(c=='@'):
        break
    print(c,end='')
'''


# continue & pass
email=input()
for c in email:
    if(c=='@'):
        print()
        continue
    else:
        pass       # pass keyword is just a place holder, performs no operation. It is null statement in python
    print(c,end='')
