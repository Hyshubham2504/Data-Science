# # Immutable objects : Int float byte string tuple
# # id command is used to return the identity of an object
# result = True
# result1 = result
# print(id(result))
# print(id(result1))
# # both id will be same because both variables are bound to same values
# result = False
# print(id(result))
# result = True
# print(id(result))  # same id as of 3rd line

a = "hello"
b = a
print(id(a))
print(id(b))
a += "ron"
print(id(a))  # its id is different that means a new object is created
print(id(b))
print()
# Mutable objects : whose contents can be changed
# mutable objects : list, dict, set, byte array#
Ingredients = ["Chicken", "Curd", "Spices", "Butter", "Ginger_Garlic"]
Ingre1 = Ingredients
print(id(Ingredients))
print(id(Ingre1))
Ingredients += ["Onion"]
print(id(Ingredients))
print(id(Ingre1))

# Strings are immutable, when we tried to change a string, python created a new object,
# a new string and reattached the name to it
# Lists are mutable, when we appended a new item, python was able to change the contents
# without creating a new object

#  buying computer parts
# current_choice = "-"
# computer = []
# while current_choice != "0":
#     if current_choice in "12345":
#         print("Adding {}".format(current_choice))
#         if current_choice == "1":
#             computer.append("1: Computer")
#         elif current_choice == "2":
#             computer.append("2: Mouse")
#         elif current_choice == "3":
#             computer.append("3: Keyboard")
#         elif current_choice == "4":
#             computer.append("4: Monitor")
#         else:
#             break
#     else:
#         print("Add options from the list")
#         print("1: Computer")
#         print("2: Mouse")
#         print("3: Keyboard")
#         print("4: Monitor")
#         print("0: to finish")
#     current_choice = input()
# print(computer)










