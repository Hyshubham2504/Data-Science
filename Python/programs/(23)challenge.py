print("Choose any one from the following options")
Menu= """1. Football 
2. Badminton 
3. Lasagna 
4. Pizaa 
5. Netflix
0. Exit"""
print(Menu)
while True:
    chosen_option=input("Choose an option")
    if chosen_option==0:
        break
    elif chosen_option in "12345":
        print("You choose {}".format(chosen_option))
    else:
        print(Menu)

