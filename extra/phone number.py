'''
Problem:

Accept a phone number as input. A valid phone number should satisfy the following constraints:
(1) The number should start with one of these digits: 6, 7, 8, 9
(2) The number should be exactly 10 digits long.
(3) No digit should appear more than 7 times in the number.
(4) No digit should appear more than 5 times in a row in the number.

If the fourth condition is not very clear, then consider this example: 
the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string valid if the phone number is valid. If not, print the string invalid.
'''


# Solution

s=input()
f=0
if s[0] in '6789' and len(s)==10 and s.isdigit():
    f=1
    k='000000'
    for i in s:
        if s.count(i)>7 or k in s:
            f=0
            break
        l=int(k)+111111
        k=str(l)
if f==1:
    print('valid')
else:
    print('invalid')

