# this is the way find max total from a file by usual file handling

'''
f=open('scores.csv','r')
scores=f.readlines()[1:]
max=0
for record in scores:
    if int(record[-4:])>max:
        max=int(record[-4:])
    # field=record.split(',')
    # print(field)
    # if int(field[8])>max:
    #     max = int(field[8])
print(max)
f.close()
'''
# Self note:
# 1. size of \n in any string is 1, not 2
# 2. when we convert a numeric string into int containing \n character at the end
# it never show any error
# ex-  int('242#') = 242     int('\n424') = 424
# but int('893#523') thorws an error


# there is some example of pandas

import pandas as pd

scores=pd.read_csv('scores.csv')
# print(scores)     # it provides data in a form of table and those table is known as dataframe
# any column in dataframe is referred as series
# print(scores.shape)     # it provides the row and column number
# print(scores['Name'])   # this will print a particular series
# print(scores['Total'].max())
# print(scores['Total'].mean())
# print(scores['Total'].sum())
# print(scores['Chemistry'].min())

# print(scores['Total'].sort_values())    # it sorts in ascending order
# print(scores['Total'].sort_values(ascending=False))    # it sorts in descending order

# print(scores.head())    # it gives first 5 rows form the dataframe
# print(scores.tail())    # it gives last 5 rows form the dataframe

# print(scores[scores['Name']=='mfglql'])     # this print all details of given data in a given series
# print(scores[scores['Gender']=='M'])    # it gives all data of having gender M

# this prints the marks of top boy and top girl
# print(scores[scores['Gender']=='M']['Total'].max())
# print(scores[scores['Gender']=='F']['Total'].max())


# categorized students in based on physics marks
# A: >85    B: 70-85    C: 60-70    D: <60
# print(scores[scores['Physics'] > 85].shape[0])
# print(scores[scores['Physics'].between(70,85)].shape[0])
# print(scores[scores['Physics'].between(60,70)].shape[0])
# print(scores[scores['Physics'] < 60].shape[0]) 



'''normal operator is not allowed in pandas, pandas has its own operators '''

subjects=['Mathematics','Physics','Chemistry']

# no of female and male students get more than 85 in individual subjects
# for sub in subjects:
#     print('Above 85 in',sub)
#     print(scores[(scores[sub] > 85) & (scores['Gender']=='F')].shape[0])
#     print(scores[(scores[sub] > 85) & (scores['Gender']=='M')].shape[0])



# no of female and male students get more than average in individual subjects
# for sub in subjects:
#     avg=scores[sub].mean()
#     print('Above avg in',sub)
#     print(scores[(scores[sub] > avg) & (scores['Gender']=='F')].shape[0])
#     print(scores[(scores[sub] > avg) & (scores['Gender']=='M')].shape[0])


'''groupby().groups feature is used to create dictionary based on given series.
it actually creates a dictionary which keys are all unique elements of the given series
and then store the index numbers into its respective keys.'''

# print(scores.groupby('Gender').groups)

for sub in subjects:
    avg=scores[sub].mean()
    print('Above avg in',sub)
    print(scores[scores[sub] > avg].groupby('Gender').groups)
    print(scores[scores[sub] > avg].groupby('CityTown').groups)

