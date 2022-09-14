low=0
high=1000
i=1
guess=0
answer=int(input("Guess any number between {} and {}".format(low,high)))
while True:
    guess=low+(high-low)//2
    if guess==answer:
        print("You got it in {} time".format(i))
        break
    if guess<answer:
        low=guess
    if guess>answer:
        high=guess
    i+=1
print(guess)

# low=0
# high=10000
# guess=1234567
# for answer in range(low,high):
#     i=1
#     low=0
#     high=10000
#     while True:
#         guess=low+(high-low)//2
#         if guess==answer:
#             print("You got {} in {} time".format(answer,i))
#             break
#         if guess<answer:
#             low=guess
#         if guess>answer:
#             high=guess
#         i+=1
