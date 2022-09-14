day="Friday"
raining=False
temp=30
#precedence---- Not>And>Or
if day=="Friday" and temp>27 and not raining:
    print("Go for swimming")
else:
    print("Learn Python")
print("-" * 80)
#or
if day=="Saturday" and temp>27 and raining:
    print("Go for swimming")
else:
    print("Learn Python")
print("-" * 80)
if day=="Saturday" and (temp>27 or not raining): #Imp
    print("Go for swimming")
else:
    print("Learn Python")
print("-" * 80)
if day=="Saturday" and temp>27 or raining:
    print("Go for swimming")
else:
    print("Learn Python")
print("-" * 80)
print()
print("-" * 80)
name=input("What is your name? ")
if name:
# if name!="":
    print("Hello, {}".format(name))
else:
    print("Are you a man with no name")
print("*" * 90)
