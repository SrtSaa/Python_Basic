import matplotlib.pyplot as plt
import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y)

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x,y)
# plt.show()



# x = np.linspace(0,20,100)
# plt.plot(x,np.sin(x))
# plt.show()



# x = np.array(["a","b","c","d"])
# y = np.array([3,8,1,10])
# plt.bar(x,y)
# plt.show()
# plt.barh(x,y)
# plt.show()



x = np.random.normal(170,10,250)
x=np.array([54,73,11,24,45,33,4])
plt.hist(x,bins=7)
plt.show()



# x = np.array(["a","b","c","d"])
# y = np.array([3,8,1,10])
# plt.pie(y,labels=x,startangle=90)
# plt.show()


'''
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,3)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,4)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,5)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()
'''



