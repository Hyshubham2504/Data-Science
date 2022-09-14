for i in range(1,15):
    print("The no. {0:2} squared is {1:3} and cube is {2:4}".format(i, i**2, i**3))
#less than sign before field width is used for left alignment and greater than for right alignment and carat(^) for centre.

print()

for i in range(1,15):
    print("The no. {0:<2} squared is {1:<3} and cube is {2:^4}".format(i, i**2, i**3))

print("division is {0:15f}".format(12/7))

print()

print("pi is approximately {0}".format(22/7)) #As default there are 15 digits after decimal point in division
print("pi is approximately {0:13}".format(22/7))
print("pi is approximately {0:18}".format(22/7))
print("pi is approximately {0:5f}".format(22/7))
#In f type case default no of digits that occurs after decimal point is 6
print("pi is approximately {0:15f}".format(22/7))
print("pi is approximately {0:20.50f}".format(22/7))
#precision is given more importance than field width
print("pi is approximately {0:52.50f}".format(22/7))
print("pi is approximately {0:72.50f}".format(22/7))
print("pi is approximately {0:72.87f}".format(22/7))
print("pi is approximately {0:<72.54f}".format(22/7))
print("pi is approximately {0:<70.51f}".format(22/7))
#Maximun precision is 51 digits after decimal point of floating type division
print(f"pi is approximately {22/7:10f}")
pi=22/7
print(f"pi is approximately {pi:10f}")
