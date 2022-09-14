import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)
y = np.sin(2 * np.pi * x)
# subplots() without arguments returns a Figure and a single Axes
fig, ax = plt.subplots(3)  # or fig, ax = plt.subplots(3, 1)
ax[0].set_title('A single plot')
ax[0].set_xlabel('0-6')
ax[0].set_ylabel('sine-curve')
ax[0].plot(x, y)
# To obtain side-by-side subplots, pass parameters 1, 2 for one row and two columns.
ax[1].set_title('Another plot')
ax[1].plot(-x, -y)
ax[2].plot(x**2, y**2)
plt.show()

x = np.linspace(0, 10, 100)
y = np.tan(4 * np.pi * x)

fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, y)
ax[0, 1].plot(-x, y)
ax[1, 0].plot(-x, -y)
ax[1, 1].plot(x, -y)
plt.show()
