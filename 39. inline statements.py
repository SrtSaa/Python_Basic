a = 10
b = 20
'''
if a<b:
    small = a
else:
    small = b
'''
small = a if a<b else b
print(small)


print('\n')


a = 5
'''
while a>0:
    print(a)
    a-=1
'''
while a>0 : print(a); a-=1


print('\n')


fruits = ['mango','apple','banana','orange','pineapple','watermelon','kiwi']
'''
l = []
for fruit in fruits:
    if 'n' in fruit:
        l.append(fruit.capitalize())
'''
l=[fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(l)