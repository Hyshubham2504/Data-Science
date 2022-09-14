# import random
# highest=1000
# answer=random.randint(0,highest)
# #print(answer)
# print("Guess a number between 0 and {}".format(highest))
# guess=0
# i=1
# while guess!=answer:
#     guess=int(input())
#     if guess<=0 or guess>=highest:
#         print("You quit")
#         break
#     if guess==answer:
#         print("You got it in {} time".format(i))
#     else:
#         if guess<answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#     i+=1







# answer=5
# guess=int(input("Guess it"))
# if guess==answer:
#     print("You guessed it in your first try")
# else:
#     if guess<answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess=int(input())
#     if guess==answer:
#         print("You guessed it correctly")
#     else:
#         print("Hardluck kid")


# guess=int(input("Please guess"))
# if guess!=answer:
#     if guess<answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess=int(input())
#     if guess==answer:
#         print("You guessed it correctly")
#     else:
#         print("You guessed it wrong")
# else:
#     print("You guessed it in your first try")

# guess=int(input("Guess a number"))
# if guess<answer:
#     print("Please guess higher")
#     guess=int(input())
#     if guess == answer:
#         print("You guessed it correctly")
#     else:
#         print("You are a sick person")
# elif guess>answer:
#     print("Please guess lower")
#     guess=int(input())
#     if guess==answer:
#         print("You guessed it correctly")
#     else:
#         print("You got a hardluck kid")
# else:
#     print("You made it in the first move")

import random
low=1
high=1000
answer=random.randint(low,high)
guess=0
i=0
while True:
    guess=int(input("guess a number between {} and {}".format(low,high)))
    if(guess<1 and guess>999):
        print("Guess out of range")
        break
    elif(guess==answer):
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



