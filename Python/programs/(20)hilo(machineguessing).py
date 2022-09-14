high=1000
low=1
print("Guess between {} and {}".format(low,high))
i=0
while True:
    i=i+1
    guess=low+(high-low)//2
    high_low=input("My guess is {}."
                   "Enter h,c or l accordingly as per your guess".format(guess))
    if high_low=="h":
        low=guess
    elif high_low=="l":
        high=guess
    elif high_low=="c":
        print("You guessed it correctly in {} times".format(i))
        break
    else:
        print("Please enter h, c, l accordingly")


