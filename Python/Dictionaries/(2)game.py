locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

Exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 1
while True:
    print(locations[loc])
    available_exits = ', '.join(Exits[loc].keys())
    if loc == 0:
        break
    chosen_exit = input("Available exits are " + available_exits + ' ').upper()
    if chosen_exit in Exits[loc]:
        loc = Exits[loc][chosen_exit]
    else:
        print("You cannot go in that direction")
