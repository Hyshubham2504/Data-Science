for i in range(1,13):
    print("The no. {:<2} square is {:<3} and cube is {:<4}".format(i,i**2,i**3))
    print("*" * 20)
#As line 2 and 3 have same indentation level so they will be a part of for loop and line 3 will also be repeated 12 times
#or
print()
for i in range(1,6):
    print("The no. {:<1} square is {:<2} and cube is {:<3}".format(i,i**2,i**3))
print("*" * 20)

print()
name=input("What is your name?")
age=int(input("What is your age, {}?".format(name)))
if age>=18:
    print("You are allowed to vote\nPlease put an X in the box")
else:
    print("Come back after {} years".format(18-age))
print()
if age<18:
    print("Come back after {} years".format(18-age))
else:
    print("You are allowed to vote\nPlease put an X in the box")

print()

name=input("What is your name?")
food=input("Whats your favourite food?")
if food=="pizza":
    print("You are liable to live, {}".format(name))
elif food=="fish":
    print("You wanna die, {}".format(name))
elif food=="chicken":
    print("You got the immortality source, {}".format(name))
else:
    print("You are not eligible to live {}\nGo to hell".format(name))


