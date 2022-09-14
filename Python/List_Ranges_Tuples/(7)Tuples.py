t = "a", "b", "c"  # Tuple
print(t)
print("a", "b", "c")
print({"a", "b", "c"})  # Tuple
# Tuple supports indexing and slicing but we cannot change the contents using assignment operator
welcome = "Welcome to my nightmare", "Alice cooper", 1975
Food = ("La Roma Pizzeria", "Tandoori chicken delight", 2019)
Sports = "Love Badminton", "Crush on Football", "Tragedy TT", 2010
imelda = "More Mayhem", "Imilda May", 2011
metallica = "Ride the lightning", "Metallica", 1974
print(Food)
print(Food[0])
print(Food[1])
print(Food[2])
# Food[0] = "Amigo"  # will show error : 'tuple' object does not support item assignment
# How to update the contents
# Tuple is an immutable object
# immutable means that u cannot change the contents once you have created a tuple
# Food = "asd", "asds"
# print(Food)
# We haven't changes the contents of the tuple Food, what we did here is we created a new tuple
# and then pointed the variable and the oder to reference it
# Advantage of tuple over list
# tuples are immutable objects required in dictionary keys
# the contents cannot be changed as of a music album containing the artists name year of release
Food = Food[0], "Four Seasons", 2018
print(Food)
Car = ["Ferrari", "Bugati", "BMW", 1950]  # List
print(Car)
Car[0] = "Audi"
print(Car)
# List is a mutable object
# title, artist = imelda  # It will give an error too many values to unpack
# as imelda contains 3 contents so we need to provide 3 stuffs for it as we have 2 here
title, artist, year = imelda
print(title)
print(artist)
print(year)
print()
# imelda.append("svsfv")  # will show error of tuple object having no attribute 'append'


print()
print("*" * 100)
print()


backstreet = "Millenium", "Nick Carter", 1990, ((1, "I want it that way"),
                                                (2, "Incomplete"), (3, "As long as you love me"),
                                                (4, "Everybody"))
print(backstreet)
title, artist, year, tracks = backstreet
print(title)
print(artist)
print(year)
print(tracks)


print()
print("*"*100)
print()


backstreet = "Millenium", "Nick Carter", 1990, (1, "I want it that way"), \
(2, "Incomplete"), (3, "As long as you love me"), (4, "Everybody")
# this back slash on line 53 is used so that 53 and 54 lines are concatenated else we would have got an error of expected 7 fields got 4
title, artist, year, track1, track2, track3, track4 = backstreet
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

print()
print("*"*100)
print()

# We know that a tuple is an immutable object and we cannot chang its content but if a list is inside a tuple then we make changes to the list

Taylor = "Reputation", "Taylor Swift", 2018, [(1, "Ready for it"), (2, "Blank Space"), (3, "I don't wanna live forever"), (4, "Look what you made me do")]
Taylor[3].append((5, "End Game"))
title, artist, year, tracks = Taylor
tracks.append((6, "ME!"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("Track number:{}\tTitle:{}".format(track, title))
