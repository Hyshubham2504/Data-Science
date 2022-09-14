Menu = []
Menu.append(["spam", "bacon", "sausage"])
Menu.append(["milk", "bacon", "apple", "lasagna"])
Menu.append(["spam", "egg", "mango", "momo"])
Menu.append(["spam", "burger", "sausage", "lamb"])
Menu.append(["lasagna", "chicken", "momo", "apple"])
print(Menu)
print()
for meals in Menu:
    # if not "spam" not in meals:
    if "spam" not in meals:
        print()
        for items in meals:
            print(items)
