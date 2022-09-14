for i in range(0,10):
    print("i is now {}.".format(i),end=' || ') #end command is used to avoid putting new line character once a command is executed
print()                                        #we can use end to put any characters as we wish after a loop is executed
for i in range(0,10,2):
    print("i is now {}.".format(i),end=' || ')
print()#if i dont use print() here then line 5 and 7s output will concatenate on the same line as we have used end command
for i in range(10): # default start value will be 0
    print("i is now {}.".format(i),end=' || ')
print()
for i in range(10,2): #as default step value is 1 so we cant go backwards there will be no output
    print("i is now {}.".format(i),end=' || ')
print()
for i in range(10,2,-1):
    print("i is now {}.".format(i),end=' || ')
print()
# for i in range(10,,-2): #invalid
for i in range(10,0,-2):
    print("i is now {}.".format(i),end=' || ')
print()
i=int(input("What is your age?")) #If i dont put int here then the system will consider everything we insert as a string and the statement will be false and the else part will print
if i in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
a=input()
print(type(a))