import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-10,10.1,.1)

# y = 3*x-4
# plt.plot(x,y)
# plt.show()


# y = x*x+2*x-15
# plt.plot(x,y)
# plt.show()


# y = 5*(x-1)*(x-2)*(x-3)
# plt.plot(x,y)
# plt.show()


# y = np.exp(x)
# plt.plot(x,y)
# plt.show()


# y = np.log(x)
# plt.plot(x,y)
# plt.show()


# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x,y)
# plt.plot(x,z)
# plt.show()

x=np.array([20,10,40,20,10,80,99,76,29,100,95,100,70,65,90,89,20,10,20,15,35,50,45,34,60])
y=np.array([80,30,30,30,5,90,100,84,100,30,92,100,74,88,93,91,40,30,25,34,25,70,55,43,67])
plt.scatter(x,y)
plt.show()