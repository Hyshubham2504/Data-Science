numbers = [3, 15, 4, 33, 56]
for number in numbers:
    if number % 8 == 0:
        print("These are unacceptable")
        break
else:
    print("You won the lottery")
# We can associate else with for loop