def is_palindrome(a):
    # s = a[::-1]
    # return s==a
    return a[::-1].casefold()==a.casefold()


print(is_palindrome('Racecar'))

def sentence_palindrome(a):
    b = ''
    for i in a:
        # if i in 'asdfghjklpoiuytrewqzxcvbnm1234567890':
        if i.isalnum():
            b = b + i
    # return b[::-1].casefold() == b.casefold()
    return is_palindrome(b)

print(sentence_palindrome('do geese see god?'))
