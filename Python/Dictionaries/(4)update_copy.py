# Words = {"rendezvous": "a meeting place",
#          "nincompoop": "a stupid person",
#          "flabbergasted": "completely shocked",
#          "oblivious": "not aware or conscious of something",
#          "supersede": "to take the place of someone not useful",
#          "abjure": "formally reject or disavow some beliefs"}
# print(Words.keys())
# Words1 = {"abstruse": "difficult to understand",
#           "apathetic": "showing no emotion",
#           "atrophy": "decrease in the size of an organ",
#           "calumny": "false accusation"}
# Words.update(Words1)  # here update method is used to add words1 dictionary to words
# # # no new dictionary is formed using update method
# print(Words.update(Words1))  # dictionaries doesn't return anything just like .sort method so we will get none here
# print(Words.keys())
# Words2 = Words.copy()
# print(Words.keys())
# print(Words2.update(Words1))
# print(Words2.keys())
# # here words2 is a new dictionary formed
# print(Words is Words2)  # false
# print(Words == Words2)  # true

print()
print("*" * 100)
print()
# Modifying the program so that we can also choose the name of the location

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

Exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

Extra = {1: {"2": 2, "3":3, "4": 4, "5": 5},
         2: {"5": 5},
         3: {"1": 1},
         4: {"1": 1, "2": 2},
         5: {"2": 2, "1": 1}}

Vocabulary = {"NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "QUIT": "Q",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
loc = 1
while True:
    print(locations[loc])
    available_exits = ', '.join(Exits[loc].keys())
    if loc == 0:
        break
    else:
        all_exits = Exits[loc].copy()
        all_exits.update(Extra[loc])
    chosen_exit = input("Available exits are " + available_exits + ' ').upper()
    if len(chosen_exit) > 1:
        words = chosen_exit.split()
        for word in words:
            if word in Vocabulary:
                chosen_exit = Vocabulary[word]
                break
    if chosen_exit in all_exits:
        loc = all_exits[chosen_exit]
    else:
        print("You cannot go in that direction")









