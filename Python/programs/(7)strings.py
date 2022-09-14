print('Its a great day to start python')
print("Python is fun")
print("Having pizza's is better than a pizza")
print('"Honesty is the best policy"')
print()
a = 'Hello'
b = "Shubham"
print(a+' '+b)
print()

name="Tim"
age=24
print(name + " is " + str(age) + " years old")
print("Tim is {0} years old".format(age))
print(name + f" is {age} years old")

# b=input('What do you love to do')
# a=input('2 magic words')
# print(a + b)
def swap_case(s):
    d = ''
    for i in s:
        if i.islower():
            i = i.upper()
        elif i.isupper():
            i = i.lower()
        d += i
    return d

print(swap_case('''HackerRank.com presents "Pythonist 2".'''))
i='h'
if i.islower():
    i = i.upper()
print(i)
print('''HackerRank.com presents "Pythonist 2".'''.swapcase())

def print_full_name(first, last):
    # Write your code here
    return "Hello {} {}! You just delved into python.".format(first, last)

print(print_full_name("Ross", "Taylor"))