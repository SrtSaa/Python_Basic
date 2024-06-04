'''
Problem:

A bot starts at the origin(0,0) and can make the following moves:
(1) UP    (2) DOWN    (3) LEFT    (4) RIGHT
Each move has a magnitude of 1 unit. Accept the sequence of moves made by the bot as input.
The first entry in the sequence is always START while the last entry in the sequence is always STOP. 

A sample sequence is given below:
START
UP
RIGHT
LEFT
LEFT
DOWN
UP
STOP

Print the Manhattan distance of the bot from the origin. 
If the bot is at the position (x, y)(x,y), then its Manhattan distance from the origin is-
D = |x| + |y|
'''


# Solution

s=input()
if s=='START':
    x=y=0
    while s!='STOP':
        s=input()
        if s=='UP':
            y+=1
        elif s=='DOWN':
            y-=1
        elif s=='LEFT':
            x-=1
        elif s=='RIGHT':
            x+=1
    print(abs(x)+abs(y))