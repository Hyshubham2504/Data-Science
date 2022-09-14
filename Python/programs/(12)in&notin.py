parrot="Norwegian Blue"
letter=input("Guess a letter")
# if letter in parrot.lower():
if letter.upper() in parrot.upper():#if we put .upper in both then we can give either lower or upper letter to check if it contains or not
    print("{} is in {}".format(letter,parrot))
else:
    print("It doesn't contain")
print("-"*80)
if letter not in parrot.casefold():#casefold converts the string into lowercase
    print("It doesn't contain")
else:
    print("{} is in {}".format(letter,parrot))