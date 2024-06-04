x='pyTHoN sTrInG MEthodS'
print(x)
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())


print("\n\n")


x='python'
print(x.islower())
x='Python'
print(x.islower())
x='PYTHON'
print(x.isupper())
x='Python'
print(x.isupper())
x='PYthOn StRiNg meTHODs'
print(x.istitle())
x='Python String Methods'
print(x.istitle())


print("\n\n")


x='123'
print(x.isdigit())
x='123abs'
print(x.isdigit())
x='asc'
print(x.isalpha())
x='asd123'
print(x.isalpha())
x='123acd'
print(x.isalnum())
x='123jd%!nh'
print(x.isalnum())
#these are bool type


print("\n\n")


#x='---pyt---hon---'
x='---python---'
print(x.strip('-'))
print(x.lstrip('-'))
print(x.rstrip('-'))
#it cuts some specific character from both side of the string but not from middle of the character


print("\n\n")


x='Python'
print(x.startswith('P'))
print(x.startswith('p'))
print(x.endswith('n')) 
print(x.endswith('N'))
#these are case sensitive and bool type


print("\n\n")


x='Python String Methods'
print(x.count('t'))            #this counts occurance of symbol
print(x.count('S'))            #this method is case sensitive

print(x.index('t'))            #this returns index position of specific value
print(x.index('t'))            #this only returns the index no where the specific values appears first

print(x.replace('S','s'))      #this replaces a specific value with another specific value   
print(x.replace('t','T'))      #it replaces all specific values present in the string

