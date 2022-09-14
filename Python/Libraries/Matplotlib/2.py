import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,2,3])
plt.show()
plt.plot([1,5,2,9],'g-o')
plt.axis([0,10,0,12]) #range of axis
plt.ylabel("Marks")
plt.xlabel("Roll no")
plt.show()
import numpy as np
a=np.arange(0,10,0.5)
plt.plot(a, a, 'r--', a,a**2,'*r',a,a**3,'go')
plt.ylabel("a,a**2,a**3")
plt.xlabel("no")
plt.axis([0,10,0,1000])
plt.show()
b=np.arange(0,100,22)
c=np.arange(1,6,1)
plt.plot(c,b,'--r',c**2,b,'b*')
plt.axis([0,30,0,100])
plt.xlabel('sub')
plt.ylabel('marks')
plt.show()


