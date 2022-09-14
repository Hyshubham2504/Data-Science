'''
import numpy as np
import matplotlib.pyplot as plt

data = [23, 45, 56, 78, 213]
#plt.bar([1,2,3,4,5], data)
#plt.bar(np.arange(5), data)
plt.bar(np.arange(5), data, color='red')

plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y,width = 0.1)
plt.show()
'''



import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y,width = 0.7)
#plt.barh(x, y)
#plt.barh(x, y, height = 0.1)
plt.show()


'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

#plt.bar(x, y, color = "red")
#plt.bar(x, y, color = "hotpink")
#plt.bar(x, y, color = "#4CAF50")
plt.bar(x, y, width = 0.1)
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

data1 = [23,85, 72, 43, 52]
data2 = [42, 35, 21, 16, 9]
#Multiple charts
#width =0.3
#plt.bar(np.arange(len(data1)), data1, width=width)
#plt.bar(np.arange(len(data2))+ width, data2, width=width)

#Stack charts
plt.bar(np.arange(5), data1)
plt.bar(np.arange(len(data2)), data2)
plt.show()
'''

'''
#Multiple Values
import numpy as np
import matplotlib.pyplot as plt
data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
'''
