i=0
while i<10:
    print("i is now {}".format(i))
    i+=1
print(i)
print("*"*80)

directions=["North","East","West","South"]
chosen_exit=""
while chosen_exit not in directions:
    chosen_exit=input("Which direction would you like to prefer?")
    if chosen_exit.casefold()== "quit":
        break
print("Its nice, finally you got a direction")