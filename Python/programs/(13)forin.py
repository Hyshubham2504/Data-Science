Parrot="Norwegian Blue"
for a in Parrot:  # We are considering what is stored inside parrot variable
    print(a)
#or
print("-"*80)
for a in "Parrot":  #We are considering only about the string parrot and not what is stored inside
    print("c")      #The loop will run 6 times with printing c 6 times
#or
print("-"*80)
for a in Parrot:  #We are considering what is stored inside parrot variable
    print("a")    ##The loop will run 6 times with printing a 14 times including space

print("-"*80)
print()

number="9,223;372:036 854,775;807"
separators="" #empty variable, It is important define it else we get an error of undefined variable
for a in number:  #Takes out each variable one by one and puts it in 19th line to chk if it is numeric or not
    if not a.isnumeric(): #If its a number then it is true but due to ifnot the statement wil be false & 21 line will execute
        separators=separators+a
print(separators)

#or
# numbers=""
# separators="" #empty variable, It is important define it else we get an error of undefined variable
# for a in number:  #Takes out each variable one by one and puts it in 19th line to chk if it is numeric or not
#     if a.isnumeric(): #If its a number then it is true but due to ifnot the statement wil be false & 21 line will execute
#         numbers=numbers+a
#     else:
#         separators=separators+a
# print(separators)
# print(numbers)


values="".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values])) #

print()
print()

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capital=""
for a in quote:
    if a.isupper():
        capital=capital+a
print(capital)
#or
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char,end='')#The end=' ' is just to say that you want a space after the end of the statement instead of a new line character.
