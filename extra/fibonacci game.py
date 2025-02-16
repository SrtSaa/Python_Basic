'''
Fibonacci likes to climb the steps either one at a time, two at a time or three at a time. 
He wants to find the total number of ways in which he can climb n steps, assuming that the order of his individual steps matters. 
Your task is to help Fibonacci compute this number.

For example, if he wishes to climb three steps, the case of n = 3n=3, he could do it in four different ways:

(1,1,1): do it in three moves, one step at a time
(1,2): do it in two moves, first take a single step, then a double step
(2,1): do it in two moves, first take a double step, then a single step
(3): do it in just one move, directly leaping to the third step

To take another example, if n = 5n=5, then some of the sequences could be:
(1, 3, 1), (1, 1, 3), (3, 1, 1), (2, 1, 1, 1), (1, 2, 1, 1), (2, 1, 2)

Each sequence is one of the ways of climbing five steps. 
The point to note here is that each element of a sequence can only be 1, 2 or 3.
'''

# Solution:

# Basic idea behind the solution:
# The sum of all steps in a sequence should add up to n
# The last term in any sequence could be either 1, 2 or 3
# The number of sequences with last step as 1 is given by steps(n - 1)
# The number of sequences with last step as 2 is given by steps(n - 2)
# The number of sequences with last step as 3 is given by steps(n - 3)
# So, total number of sequences is steps(n - 1) + steps(n - 2) + steps(n - 3)

def steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return steps(1) + steps(2) + 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
