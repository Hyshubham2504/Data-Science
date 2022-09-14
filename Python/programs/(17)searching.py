Foodlist=["Pizza","Burger","Butter Chicken","Lasagna","Biryani","Dal Makhani","Matar Paneer"]
print("Menu = {}".format(Foodlist))
Food_To_Find=input("What would you like to have?")
found_at=None  # If I would have put something else against lasagna and would not have declared found_at variable i will
# get an error of undefined variable
for index in range(len(Foodlist)):
    if Foodlist[index]==Food_To_Find:
        found_at=index
        break  # used to terminate the loop after we have found what we needed, basically to stop the loop from flowing
        # again making it more efficient
print("Food was found at {}".format(found_at))
#or
print("*"*70)
if Food_To_Find in Foodlist:
    found_at=Foodlist.index(Food_To_Find)
if found_at is not None:
    print("{} was found at {}".format(Food_To_Find,found_at))
else:
    print("{} was not found".format(Food_To_Find))
