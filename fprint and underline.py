price = [20.02,86.92,1.88]      
meal = ['breakfast','lunch','supper']  

# whenver '\033[4m\0' this term appears it starts underlining and
# when '\033[0m' this term appears it stops undelining
for x in range(len(meal)):
    # price.append(float(input(f"Enter cost of {meal[x]}: $\033[4m\0")))   # here we underline the user input portion
    print('\033[0m', end='')      # after taking input we stop underlining
    meal[x] = meal[x].capitalize()      


total = sum(price)   	# it is the total of all meals' price
len_total = len(str(total))     # this is the length of total price

# here we calculate which price's and meal's length is bigger 
max1 = max2 = 0
for i in range(len(meal)):
    if len(str(meal[i]))>max1:
        max1 = len(str(meal[i]))
    if len(str(price[i]))>max2:
        max2 = len(str(price[i]))
max2 = max(max2, len_total)


# here ":<" is used for left align and the number followed by ":<" is used for how space it will allocate for the output
# and ":>" is used for right align and the number followed by ":>" is used same as previous

print(f"\n\n{'Meal':<{max1+4}}Cost")    
for i in range(0,len(meal)):
    print(f"{meal[i]:<{max1+4}}${price[i]:>{max2}}")
print(f"{'Total':<{max1+4}}${total:>{max2}}")   