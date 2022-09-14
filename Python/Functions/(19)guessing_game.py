import random
low=1
high=1000
answer=random.randint(low,high)
print(answer)
guess=0
i=0

def get_integer_range():
    while True:
        temp = input("Guess a number between {} and {}".format(low,high))
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{} is not a number".format(temp))

while True:
    # guess=input("guess a number between {} and {}".format(low,high))
    guess = get_integer_range()
    if(guess==answer):
        print("You guessed in {} times".format(i))
        break
    else:
        if(guess<answer):
            print("guess higher")
            low=guess
        else:
            print("guess lower")
            high=guess
        i+=1



