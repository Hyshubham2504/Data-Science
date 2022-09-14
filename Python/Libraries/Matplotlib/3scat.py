import matplotlib.pyplot as plt
import numpy as np
# dataset1
x1=np.arange(0,100,13)
y1=np.arange(0,45,6)
#data set2
x2=np.arange(0,200,24)
y2=np.arange(0,300,35)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.scatter(x1,y1,c="green",marker='*',s=50)
plt.scatter(x2,y2,c="blue",marker='s',s=25)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.colorbar()
plt.show()

