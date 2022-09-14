my_list = list(range(20))
print(my_list)
print(range(10))
print()
even = list(range(0, 10, 2))
print("even = {}".format(even))
print("odd = {}".format(list(range(1, 10, 2))))
print()
alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha.index("e"))
print(alpha[4])
print()
small_decimals = range(1, 200)
print(small_decimals.index(5))
print(small_decimals[6])
my_range = small_decimals[1:50:3]
print(list(my_range))
print(my_range.index(5))
print(my_range[5])
print()
eights = range(8, 1000000, 8)
print(eights.index(16))
# guess = int(input("Guess any no. between 8 and one million"))
# if guess in eights:
#     print("{} is divisible by 8.".format(guess))
# else:
#     print("[] is not divisible by 8.".format(guess))
# print()
x = range(3, 40, 3)
for i in x:
    print(i, end=" ")
print()
for i in range(0, 40, -3):
    print(i, end=" ")
print()
print(x == range(3, 40, 3))
print()
print(range(0, 5, 2) == range(0, 6, 2))
print()
r = range(0, 30, -2)
print(list(r))  # We get no output here because
# in case of negative step in range function, start value must be greater than stop value
# its different from slice as it changes the sequence according to the step
# in range, the negative step doesnt reverse the sequence so we cant go from 0 to 29 backwards
y = range(0, 100)
print(list(y[10:50:-3]))
for i in y[::-2]:
    print(i, end=' ')
print()
for i in range(100, 0, -2):
    print(i, end=' ')
print()
print(range(0, 100)[::-2] == range(99, 0, -2))
backstring = "egaugnal lufrewop yrev a si nohtyP"
print(backstring[::-1])
print()
for i in range(0, 10)[::-1]:
    print(i, end=' ')
print()










