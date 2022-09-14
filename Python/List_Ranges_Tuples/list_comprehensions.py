import math
import pickle
from collections import defaultdict
print([x for x in range(10)])
print()
print([(x, x**2) for x in range(10)])
print()
print([x for x in range(20) if x % 3 == 0])
print()
print([x if x % 2 == 0 else 'odd' for x in range(10)])
print()
print(['{} = odd'.format(x) if x % 2 != 0 else '{} = even'.format(x) for x in range(10)])
print()
a = []
b = []
c = []
print([[j for j in range(1, 6)] for i in range(1, 6)])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [subvalue for sublists in matrix for subvalue in sublists]
print(matrix)
print(flattened_matrix)
# Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
print([a for sublists in planets for a in sublists if len(a) < 6])
print()
print([str(x) * x for x in range(10)])
print()
# dict_comprehensions
print({x: x**2 for x in range(5)})
print({x: math.sqrt(x) for x in range(10)})
print()
d = {x: (math.sqrt(x), x**2) for x in range(1, 6)}
print(d)
# inverting keys and values
invert_d = {a: b for b, a in d.items()}
print(invert_d)
print()
# multiple if-else in list comprehensions
print([(x, x**2) if x % 3 == 0 else 10 if x % 3 == 1 else 5 for x in range(10)])
print()
friends = {'Chandler': 'Me', 'Joey': 'Funny', 'Rachel': 'Cute', 'Ross': 'Doctor'}
friends_home = {'Chandler': 'Ohio', 'Joey': 'Rome', 'Rachel': 'California', 'Ross': 'New York'}
with open('friends.pkl', 'wb') as f:
    pickle.dump(friends, f)
with open('friends.pkl', 'rb') as f:
    new_friends = pickle.load(f)
print(new_friends)
friends2 = {a: (friends[a], friends_home[a]) for a in friends}
print(friends2)
# print(friends2['mike']) # error
print(friends2.get('mike'))
print(friends2.get('mike', 'non-existent friend'))
# Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the
# dict class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost
# same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does
# not exists.
# defaultdict
print()
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1  # if u cant understand the output then use print(d) and check the output
print(d)
print()
def_dict = defaultdict(int)
print(def_dict)  # empty dictionary
print(int())
print(def_dict['jane'])  # when we use a key which doesnt exist, it invokes the int function whose value is 0 and key
# becomes a part of dictionary with value 0
def_dict['Jane'] += 1  # so in this case def_dict['Jane'] = def_dict['Jane'] + 1 (here def_dict['Jane']=0)
print(def_dict)
def_dict['Ronaldo'] += 100
def_dict['Messi']
def_dict[1]
print(def_dict)
print()
list_def_dict = defaultdict(list)
list_def_dict[1]
list_def_dict[2, 3]
list_def_dict[2].append([4, 6, 7, 8])  # if i dont include square brackets i dont get any value
list_def_dict[1].append(123)
print(list_def_dict)
print()
#  setting a default value for a missing key
e = defaultdict(lambda: 16)
print(e[3])