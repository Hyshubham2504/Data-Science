string = "1234567890"
print(iter(string))  # It shows the representation of an iterable object
print(next(iter(string)))
print(next(iter(string)))
iterable_string = iter(string)  # Now we can iterate the variable string and print all the elements by using next function
print()
print(iterable_string)
print(next(iterable_string))
# If i will print next(string) i will get an error as string is not an iterable object
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
print(next(iterable_string))
# print(next(iterable_string))  # so the for char in iterable_String could print what was left
# print(next(iterable_string))  # It will show error because in case of iterators it will look for the next element which is not there
# In case of for loop it directly terminates the loop after the last element
print()
for char in iter(string):
    print(char)
print()
for char in iterable_string:  # doesnt show any output
# because iterable_string has already printed all the stuffs inside "string"
# now it doesnt have anything to print
    print(char)

# ***challenge***

Food = ["Lasagna", "Burger", "Eggs", "Chicken", "Pizza"]
iter_object = iter(Food)
for a in range(len(Food)):
    # print(next(iter(Food)))  # In this case we will get lasagna printing over 5 times iter function is used to be explicitly
    print(next(iter_object))
# If we use next function on iterable object created explicitly we traverse through the next element
