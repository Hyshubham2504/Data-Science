import numpy as np
import matplotlib.pyplot as plt
lang = np.array(['java', 'python', 'php', 'javascript', 'c#', 'c++'])
pop = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
plt.bar(lang, pop, width=0.5, color='blue')
plt.xlabel('language')
plt.ylabel('popularity')
plt.title('Popularity of programming languages worldwide')
plt.show()
