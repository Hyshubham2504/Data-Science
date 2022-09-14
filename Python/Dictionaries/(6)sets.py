# farm_animals = {'horse', 'cow', 'goat'}
# print(farm_animals)
# wild_animals = set(['lion', 'tiger', 'leopard'])
# wild_animals.add('dinosaur')
# print(wild_animals)
# # sets are unordered
# empty_set = set()
# # empty_set = {} its a dictionary not a set
# print(empty_set)
# empty_set.add('pizza')
# print(empty_set)
even = set(range(0, 40, 2))
print(even)
squares_tuple = (1, 4, 9, 16, 25)
squares_set = set(squares_tuple)
squares_set.add(36)
print(squares_set)
print()
print(even.intersection(squares_set))
print(even & squares_set)
print(squares_set.intersection(even))
print(squares_set & even)
print()
print(sorted(even))
print(sorted(squares_set))
print(sorted(even.difference(squares_set)))
print(sorted(even-squares_set))
print(sorted(squares_set.difference(even)))
print(sorted(squares_set-even))
# using difference keyword is better as we will be know if we are
# dealing with sets or what
def mult(numbers):
    new_list = [no * 10 for no in numbers]
    return new_list
numbers=[1,2,3]
print(mult(numbers))
