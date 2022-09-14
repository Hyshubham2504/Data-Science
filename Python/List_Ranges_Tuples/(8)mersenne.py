# A Mersenne number is any number that can be written as  (2**𝑝)−1  for some  𝑝 .
# For example, 3 is a Mersenne number ( 2^2−1 ) as is 31 ( 2^5−1 ).
# Mersenne numbers can only be prime if their exponent,  𝑝 , is prime.

def mersenne_no(p):
    return 2 ** p - 1
print(mersenne_no(4))
# list of mersenne no.s between 3 and 65

def mer():
    list1 = []
    for i in range(1,100):
        if 3<=mersenne_no(i)<=65:
            list1.append(mersenne_no(i))
    return list1
print(mer())

# list of primes p between 3 and 65 where 2**p-1 is a prime no. for p >=3 and <=65
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
print(is_prime(97))

def mer_range():
    list1=[]
    list2=[]
    for i in range(3,65):
        if is_prime(i):
            list1.append(i)
    for i in list1:
        list2.append(2**i-1)
    return list2
print(mer_range())

#lucas-lehmer

# We can test if a Mersenne number is prime using the Lucas-Lehmer test. First let's write a function that
# generates the sequence used in the test. Given a Mersenne number with exponent  𝑝 , the sequence can be defined as
# 𝑛0=4
# 𝑛𝑖=(𝑛(i-1)**2−2)𝑚𝑜𝑑(2𝑝−1)
# Write a function that accepts the exponent  𝑝  of a Mersenne number and returns the Lucas-Lehmer sequence up
# to  𝑖=𝑝−2  (inclusive). Remember that the modulo operation is implemented in Python as %.

def lucas_lehmer(p):
    ll=[4]
    for i in range(1,p-1):
        n=(ll[i-1]**2-2)%mersenne_no(p)
        ll.append(n)
    if(ll[p-2]==0):
        print("{} is a mersenne prime no.".format(mersenne_no(p)))
    return ll
print(lucas_lehmer(7))

# def is_prime(n):
#     if n==2 or n==3: return True
#     if n%2==0 or n<2: return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(117))

# Exercise 3: mersenne_primes
# For a given Mersenne number with exponent  𝑝 , the number is prime if the Lucas-Lehmer series is 0 at position  𝑝−2 .
# Write a function that tests if a Mersenne number with exponent  𝑝  is prime. Test if the Mersenne numbers with prime
# 𝑝  between 3 and 65 (i.e. 3, 5, 7, ..., 61) are prime. Your final answer should be a list of tuples consisting of
# (Mersenne exponent, 0) (or 1) for each Mersenne number you test, where 0 and 1 are replacements for False and True
# respectively.
# HINT: You may want to use the zip function which returns an iterable of tuples resulting in a pair-wise combination
# of two iterables (e.g., two lists).

def prime_list(a,b):
    list1=[]
    for i in range(a,b+1):
        if is_prime(i):
            list1.append(i)
    return list1
primes = prime_list(3,65)
print(primes)

def mer_prime_test():
    list2=[]
    for j in primes:
        ll=[4]
        for i in range(1,j-1):
            n=(ll[i-1]**2-2)%mersenne_no(j)
            ll.append(n)
        if ll[j-2]==0:
            list2.append(1)
        else:
            list2.append(0)
    return list2
mers_p=mer_prime_test()
print(mer_prime_test())

mersenne_primes=list(zip(primes,mers_p))
print(mersenne_primes)

# Exercise 5: sieve
# In this problem we will develop an even faster method which is known as the Sieve of Eratosthenes
# (although it will be more expensive in terms of memory). The Sieve of Eratosthenes is an example of dynamic
# programming, where the general idea is to not redo computations we have already done (read more about it here).
# We will break this sieve down into several small functions.
#
# Our submission will be a list of all prime numbers less than 2000.
#
# The method works as follows (see here for more details)
#
# Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime
# Starting with  𝑝=2  (the first prime) mark all numbers of the form  𝑛𝑝  where  𝑛>1  and  𝑛𝑝<=𝑁  to be not prime
# (they can't be prime since they are multiples of 2!)
# Find the smallest number greater than  𝑝  which is not marked and set that equal to  𝑝 , then go back to step 2.
# Stop if there is no unmarked number greater than  𝑝  and less than  𝑁+1
# We will break this up into a few functions, our general strategy will be to use a Python list as our container
# although we could use other data structures. The index of this list will represent numbers.
#
# We have implemented a sieve function which will find all the prime numbers up to  𝑛 . You will need to implement the
# functions which it calls. They are as follows
#
# list_true Make a list of true values of length  𝑛+1  where the first two values are false (this corresponds with step
# 1 of the algorithm above)
# mark_false takes a list of booleans and a number  𝑝 . Mark all elements  2𝑝,3𝑝,...𝑛  false (this corresponds with step
# 2 of the algorithm above)
# find_next Find the smallest True element in a list which is greater than some  𝑝  (has index greater than  𝑝  (this
# corresponds with step 3 of the algorithm above)
# prime_from_list Return indices of True values
# Remember that python lists are zero indexed. We have provided assertions below to help you assess whether your
# functions are functioning properly.

def list_true(n):
    my_list = [True] * (n+1)
    my_list[0], my_list[1] = False, False
    return my_list
print(list_true(10))
assert list_true(5)==[False, False, True, True, True, True]

def mark_false(bool_list, p):
    for i in range(2*p, len(bool_list), p):
        bool_list[i] = False
    return bool_list
print(mark_false(list_true(10), 3))

def find_next(bool_list, p):
    list1 = enumerate(bool_list[p+1:],start=p+1)
    for i, j in list1:
        if j:
            return i
    return None
assert find_next(list_true(10), 2) == 3

def prime_filter(bool_list):
    return [i for i, j in enumerate(bool_list) if j==True]
assert prime_filter([False, False, True, True, False, True]) == [2,3,5]

def sieve(n):
    bool_list = list_true(n)
    p=2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_filter(bool_list)

print(sieve(100), len(sieve(100)))







