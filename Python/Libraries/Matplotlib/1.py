import matplotlib.pyplot as plt
import numpy as np
# x=[0,6] #pyplot-pyhton plot subpackage
# y=[0,250]
# plt.plot(x,y)
# plt.show()
x1 = np.linspace(0, 10, 100)  # here 100 means the no. of samples generated
print(x1)
y1 = 2 * x1
plt.plot(x1, y1, '-', linewidth=3, color='red')
plt.xlabel('x1')
plt.ylabel('y1')
plt.axis([0, 15, 0, 30])
plt.title('prac')
plt.show()
