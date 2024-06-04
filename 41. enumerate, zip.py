fruits = ['mango','apple','banana','orange','pineapple','watermelon','kiwi']
size = [5, 2, 6, 7, 4, 5, 2]

# enumerate is used to print the element of the list with its index
for f in enumerate(fruits):
    print(f)
print()


# zip is used to merge lists in a form tuple
print(list(zip(fruits,size)))
print()
print(dict(zip(fruits,size)))
print()
