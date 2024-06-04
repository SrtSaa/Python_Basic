file = open('sample.txt','r')
for line in file:
    if 'EMAIL' in line:
        print('True')
    else:
        print('false')
file.close()