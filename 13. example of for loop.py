'''
# sum of first n positive integers

n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)
'''



'''
# multiplication table

n=int(input())
for i in range(1,11):
    print(n,' X ',i,' = ',n*i)
'''


'''
# print in decreasin order

for i in range(10,-1,-1):
    print(i)
'''


# for loop without range
country='India'
for letter in country:
    print(letter)