import random as rd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

l_late=[]   # this list contains the no of late passenger for each train

for i in range(100000):      # this loops runs for 10 times for 10 trains
    current_load=0          # for each tarin no of passenger in the beginning is 0
    late_pass=0             # this keeps record no of late passenger in each train
    for j in range(5):      # this loops runs for 5 times as no of stops are 5 before reaching the final stations
        x=rd.randint(0,100) # we generate a random number between 1 and 100, which will attempt to get the train in a station
        #print(x,end=' ')
        current_load+=x                 # first all board the train
        if current_load>250:            # if current load is greater than 250
            diff = current_load - 250   # we have to reduce extra passenger
            late_pass+=diff             # and those extra passengers are consiedered as late passenger
    l_late.append(late_pass)        # we append that late passenger into l_late list for each train
    #print()

l_late = np.array(l_late)
avg = np.mean(l_late)           # this is the average number of late passenger per train
print('\nThe average number of late passenger per train = ',avg)            



# 95% confidence interval for the true value of the average based on our simulation

print("\n95% confidence interval = ",end='')
print(stats.t.interval(alpha=0.95, loc = np.mean(l_late), df = len(l_late)-1, scale = stats.sem(l_late)))
# previous line is the syntax to find out 95% confidence interval
# you can also use the following method
'''
n = len(l_late)
mean = np.mean(l_late)
sem = stats.sem(l_late)
z = stats.t.ppf((1+0.95)/2,n-1)
h = sem*z
print(f'95% confidence interval = ({mean-h}, {mean+h})')
'''



# Histogram showing the frequencies of each amount of late passengers.

plt.hist(l_late, edgecolor='black')                         # this is used to plot the histogram
plt.title('Frequencies of late passenger for each train')   # this is used to give the title
plt.xlabel('No of late passenger')                          # this is used to label X axis
plt.ylabel('Count')                                         # this is used to label Y axis
plt.show()                                                  # this is used to show the plot