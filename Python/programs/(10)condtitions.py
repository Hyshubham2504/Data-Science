age=int(input("How old are you? "))
if age>=16 and age<=64:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("_" * 50)
print()
if 16<=age<=64:
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("_"*50)
print()
if age<=16 or age>=64:
    print("Enjoy your free time")
else:
    print("Have a good day at work")