import matplotlib.pyplot as plt
import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y,width = 0.1)
# plt.barh(x, y)
# plt.barh(x, y, height = 0.2)
# plt.show()

# data = [23, 45, 56, 78, 213]
# plt.bar([1,2,3,4,5], data, color='blue', width=0.30)
# plt.bar(np.arange(5), data, color='black',width=0.15)
# plt.bar(np.arange(5), data, color='red',width=0.075)
# plt.show()

#multiple charts

# d1=np.array([23,45,67,89,12])
# d2=np.array([120,35,61,84,60])
# w1=0.2
# plt.bar(np.arange(len(d1)),d1,color='blue',width=w1)
# plt.bar(np.arange(5)+w1,d2,color='black',width=w1)
# plt.show()

#stack charts
#1st code
# d1 = [13,2, 3, 4, 5]
# d2 = [6, 7, 8, 9, 10]
# d1 = [23,85, 72, 43, 52]
# d2 = [42, 35, 21, 16, 9]
# plt.bar(np.arange(5), d1)
# plt.bar(np.arange(len(d2)), d2, bottom=d1)
# plt.show()

#2nd code
# A = [5., 30., 45., 22.]
# B = [5., 25., 50., 20.]
#
# X = range(4)
#
# plt.bar(X, A, color = 'b')
# plt.bar(X, B, color = 'r', bottom = A)
# plt.show()

marks=[[50,64,6,87],[30,43,99,15],[12,21,16,61],[89,98,67,76]]
# w1=0.2
# plt.bar(np.arange(4),marks[0],width=w1)
# plt.bar(np.arange(4)+w1,marks[1],width=w1)
# plt.bar(np.arange(4)+2*w1,marks[2],width=w1)
# plt.bar(np.arange(4)+3*w1,marks[3],width=w1)
# plt.show()
#
a=plt.figure()
X=np.arange(4)
a1=a.add_axes([0,0,1,1])
a1.bar(X + 0.00, marks[0], color = 'b', width = 0.25)
plt.show()

marks=[[50,64,6,87],[30,43,99,15],[12,21,16,61],[89,98,67,76]]
w1=0.2
for i in range(4):
    plt.bar(np.arange(4)+i*w1, marks[i],width=w1)
plt.show()