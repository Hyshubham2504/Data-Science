Words = {"Forsake": "To leave a person or place", "Entice": "To persuade somebody to do something", "Chivalry": "polite behaviour towards women by men",
         "Narcissist": "One who admire themselves", "Snitch": "Inform on someone", "Knack": "Ability to do things easily"}
print(Words)
print(Words["Chivalry"])
print()
print("Forsake: {}\nNarcissist: {}".format(Words["Forsake"], Words["Narcissist"]))
Words["Nostalgia"] = "Feeling pleasure while thinking of happy times in the past"
print(Words)
print("Nostalgia: {}".format(Words["Nostalgia"]))
Words["Snitch"] = "Steal"  # If we add a key with an existing name like here snitch, the key just gets updated
print(Words)
print()
print("*"*100)
print()
Birth = {"Shubham": "April", "Tushar": "September", "Aditya": "August",
         "Ajay": "July", "Simran": "January", "Love": "December", "Aditya": "September"}
print(Birth)  # Aditya: "September
# In this case there are two keys with the same name so the key at the end will overwrite the previous one
print("*" * 100)
print()
del Words["Nostalgia"]  # del is used to remove keys and can delete the whole dictionary Words here in this case
print(Words)
# del Words  # will delete the dictionary 'Words'
# print(Words)  # will show error of name words is not defined
# Words.clear()  # will remove only the contents of the dictionary
# print(Words)  # Output: {}
description = Words.get("Narcissist")  # another way to print the contents inside the key
print(description)

# while True:
#     keys = input("Enter a word")
#     if keys == "quit":
#         break
#     if keys in Words:
#         # desc = Words[keys]
#         desc = Words.get(keys)
#         print(desc)
#     else:
#         print("We don't have " + keys)
# desc = Words.get(keys, "We don't have " + keys )
# we can use this code in the if statement above, it will eliminate the use of else statement
# if a key is found then it will print that key and if not then the 2nd part will be printed
# which is the default part or else part
# If we enter any key that is not in the dictionary then we will either get the else statement here or 'none'
print()

# ordered_keys = list(Words)
# ordered_keys.sort()
# for i in ordered_keys:
#     print(i + ": " + Words[i])
# or

# ordered_keys2 = sorted(list(Words.keys()))
# ordered_keys2 = sorted(Words, reverse=True)
# for i in ordered_keys2:
#     print(i + ": " + Words[i])

print()
print("*"*100)
print()

for i in sorted(Words, reverse=True):
    print(i + ': ' + Words[i])
print()
Words2 = Words
print(Words2)
print()
print(Words2.values())
print()
print(Words2.keys())
print()
Words2["Plagiarism"] = "One who steals someone original work"
print(Words2["Plagiarism"])
print(sorted(Words.keys()))  # It states that when we assigned Words to words2,
# so any changes made in words2 will reflect a change in words
print()
Words3 = Words.keys()  # Here words3 is a view object
# We cannot make changes to it
print(Words3)
Words["Ort"] = "Leftover food"
print(Words3)
# print(Words3["Ort"])  # will give an error
print(Words["Ort"])
print()
print(Words.items())
print()
tuple1 = tuple(Words.items())  # way to change into a tuple
print(tuple1)
print()
for a in tuple1:
    word, meaning = a
    print(word + ': ' + meaning)
print()
# to convert tuple into dictionary we use dict function
print(dict(tuple1))
print()
# JOINS
my_list = ["1", "2", "3", "4"]
numbers = "1234567890"
new_string = ' : '.join(numbers)
new_string1 = ', '.join(my_list)
print(new_string)
print(new_string1)
