# Ip_address=input("Enter the ip address:")
Ip_address="192.142.6.88"
print(Ip_address.count("."))
print(Ip_address.count("1"))
print(Ip_address.count("")) #shows one more character
print(len(Ip_address))
print(Ip_address.count("1" and "8"))  # if we have both "1" and "8" 2 times then we
# will get output 2
print(Ip_address.count("1" or "5"))
print(Ip_address.count("1" and "5"))
print()
Ingredients = ["Chicken", "Curd", "Spices", "Butter", "Ginger_Garlic"]
print(Ingredients[0:3])  # slicing a list produces another list
print(Ingredients[-1])  # last item
Ingredients.append("Onion")  # Append is used to add item at the end of a line or list
for Ingredient in Ingredients:
    print("Butter Chicken needs {}".format(Ingredient))
print(Ingredients)
print()
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = odd + even
print(numbers)
print(len(even))
print(min(even))
print(max(odd))
print("mississippi".count("iss"))
# ordered_list = numbers.sort()
# print(ordered_list)  # It will show none because .sort is used on existing variables and no new object is created
# print(numbers)  # we will get a sorted list
# printing ordered_list will produce none but .sort actually sorts the list numbers
numbers1 = sorted(numbers)
print(numbers1)
print()
if numbers == numbers1:  # Both lists are not equal even though having same entities because they are not in same order
    print("Both lists are equal")
else:
    print("Both lists are not equal")

if sorted(numbers) == numbers1:  #if sorted(numbers) == numbers1.sort(): here .sort() will produce none so false statement
    print("Both lists are equal")
    print(sorted(numbers))
    print(numbers1.sort())
else:
    print("Both lists are not equal")
numbers.sort()
print(numbers)

#.sort is used on existing variable and sorted is used for new variable
a = enumerate([False, False, True, True, True, True, True, True, True, True, True, True], start=4)
print(list(a))
d = "ABCDCDC"
print(d.count('CDC'))