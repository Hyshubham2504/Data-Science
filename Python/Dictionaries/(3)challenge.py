# Modify the program so that the exits is a dictionary rather than a list
# with the keys being the numbers of the locations and t    he values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys and their values will be
# a single letter that the program can use to determine which way to go.

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

Vocabulary = {"NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "QUIT": "Q"}
loc = 1
while True:
    print(locations[loc])
    available_exits = ', '.join(Exits[loc].keys())
    if loc == 0:
        break
    chosen_exit = input("Available exits are " + available_exits + ' ').upper()
    if len(chosen_exit) > 1:
        words = chosen_exit.split()
        for word in words:
            if word in Vocabulary:
                chosen_exit = Vocabulary[word]
                break
        # for word in Vocabulary:
        #     if word in chosen_exit:
        #         chosen_exit = Vocabulary[word]
    if chosen_exit in Exits[loc]:
        loc = Exits[loc][chosen_exit]
    else:
        print("You cannot go in that direction")

print()
# using split function
print(locations[0].split())  # here the default delimiter is space so it separates them
# into words separated by words
print(locations[3].split(","))  # here the delimiter is comma
print(' '.join(locations[0].split()))