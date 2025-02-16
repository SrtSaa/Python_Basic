# Problem:

# Accept a string as input. If the input string is of odd length, then continue with it. 
# If the input string is of even length, make it odd length by following the two steps:
# (1) If the last character is a period (.), then remove it
# (2) If the last character is not a period, then add a period (.) to the end of the string

# Call this string of odd length 'word'.
# Select a substring made up of three consecutive characters from word 
# such that there are an equal number of characters to the left and right of this substring. 
# Print this substring as output. 
# You can assume that all input strings will be in lower case and will have a length of at least four.



#solution:

word=input()
a=len(word)
if(a%2==0):
    if word[-1]=='.':
        a-=1
    else:
        word+='.'

print(word[a//2-1],end="")
print(word[a//2],end="")
print(word[a//2+1])