# initialize the variables
current = 1
end = 10

# the loop runs while current is less or equal to end
while current <= end: 
    print(current)      # print the value of current
    
    # if current is equal to end, it means it has reached at end
    if current == end:
        print("You have reached the end")  
        # the above block will execute if and only if 'current' is equal to 'end'. Otherwise it will not execute
    
    # increase the value of current after each execution
    current += 1
