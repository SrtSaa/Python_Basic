'''
import calendar

#print(calendar.month(2022,2))
print(calendar.calendar(2022))
'''


'''
from calendar import *
print(month(2022,10))
print(calendar(2022))
'''


'''
from calendar import month
print(month(2022,2))
#print(calendar(2022))      #this will not occur because only month is imported
'''


'''
from calendar import month, calendar
print(month(2022,2))
print(calendar(2022))   #now this line will execute
'''


'''
import calendar as c        #it helps to use long library name in short form

print(c.calendar(2022))
'''


'''
from calendar import month as m
print(m(2022,2))
'''

