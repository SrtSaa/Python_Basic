fruits = ['mango','apple','banana','orange','pineapple','watermelon','kiwi']

for i in fruits:
    print(i)

print()
print()
# in for loop all elements are executed at a time
# but we can stop printing after executing first element
# after some time we can start printing where we left the list using iterator

basket = iter(fruits)

print('first execution')
print(next(basket))
print('\nsecond execution')
print(next(basket))
print('\nthird execution')
print(next(basket))
print('\nfourth execution')
print(next(basket))

# if we execte this after finishing the list it will thorw an error