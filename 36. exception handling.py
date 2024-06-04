from logging import exception


a = int(input())
b = int(input())
# c = a/b
# previous line throw an error if b is 0

try:
    c = a/b
    print(c)
    #print(d)
    f = open('test.csv','r')
except ZeroDivisionError:
    print('Invalid input. Divisor cannot be 0')
except NameError:
    print("variable is not defined")
except FileNotFoundError:
    print('Invalid file name. Please check again')
except:     # if other than given exception blocks appears
    print('Something went wrong')

# if the program stops somewhere in the middle of program for the exception this part will still execute
finally:    
    f.close()
    # print(d)
    # if exception occurs in the code in the finally block
    # it will throw an error



# create own exception
a = int(input())
if a<18:
    raise Exception('You are underage')
