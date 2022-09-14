list1 = []
list2 = list()
print("List 1 : {}".format(list1))
print("List 2 : {}".format(list2))
if list1 == list2:
    print("Both lists are equal")
print(list1 is list2)  # list 2 here is a constructor list so it actually returns us a new list
print(list("Hello Shubham"))
print()

even = [2, 4, 6, 8]
even1 = even
# even1 = list(even)  # as it is a constructor list so it returns a new list
# print(even is even1)  # false
even1.sort(reverse=True)
print(even)
print(even1)
print(even is even1)
print(even == even1)

# In this case we are assigning even list to even1 list, so if we update even1 list indirectly the even list will also be updated
print()
print("*" * 100)
print()
odd = [1, 3, 5, 7, 9]
odd1 = sorted(odd, reverse=True)  # This is a type of constructor list which actually creates a new separate list
print(odd)
print(odd1)
print(odd is odd1)  # here (is) compares the two lists
print(odd == odd1)  # == compares the inner contents
# In this case we are assigning the list odd to odd1 as it is a constructor list so it makes a separate list
# and any changes made in the odd1 list will not reflect any changes in the odd list
print()
Junk = ["Pizza", "Burger", "Lasagna", "Maggi", "Momo"]
Healthy = ["Apple", "Vegetables", "Juice", "Chicken"]
Food = [Junk, Healthy]  # concatenating junk and healthy lists into
print(Food)
for food_type in Food:
    print(food_type)
    for stuffs in food_type:
        print(stuffs)
new=[1,2,3,4]
new1=[5,6,7]
new.extend(new1)
new.insert(2,9)
new.remove(6)
print(new)
# cmd = input()
# print(cmd)
import datetime
print(datetime.date(1970, 1, 1).strftime('%Y-%d-%B'))

inp = 'rqwr7fh'
print(any(x.isalnum() for x in inp))
print(any(x.isalpha() for x in inp))
print(any(x.isdigit() for x in inp))
print(any(x.islower() for x in inp))
print(any(x.isupper() for x in inp))

# The any() function returns a boolean value:
# True if at least one element of an iterable is true
# False if all elements are false or if an iterable is empty

str = 'rqwr7fh'
arr = [False]*5

for letter in str:
    if letter.isalnum():
        arr[0] = True
    if letter.isalpha():
        arr[1] = True
    if letter.isdigit():
        arr[2] = True
    if letter.islower():
        arr[3] = True
    if letter.isupper():
        arr[4] = True

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print()
string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

a = []
b = ''
c = 0
def wrap(string, max_width):
    a = []
    b = ''
    c = 0
    for i in range(len(string)):
        b += string[i]
        c += 1
        if c==max_width:
            a.append(b)
            b = ''
            c = 0
        if i == len(string) - 1:
            a.append(b)
    return '\n'.join(i for i in a)
result = wrap(string, max_width)
print(result)
#or

import textwrap

print(textwrap.fill(string,max_width))