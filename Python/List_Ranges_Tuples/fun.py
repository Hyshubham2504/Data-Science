def fn1():
    print("test")

def fn2(a):
    for i in range(a):
        print(i)
def fn3(a):
    return 1/a
def logn(orz):
    print(orz)
def proc(a,b):
    print(a+b)
def calc(a,b):
    return a*b
fn1()
fn2(5)
print(fn3(5))
logn('abc')
logn('kiit')
proc(23,33)
proc('23','33')
calc(12,13)
print(calc(12,13))
print(27**1/3)
print(27**(1/3))
print(15/2*3)
print(15//2*3)

# def sumsub(a,b,c=0,d=0): initialization should be done from right to left
def sumsub(a, b, c=0, d=0):
    return a-b+c-d
print(sumsub(42,15,d=10))
# print(sumsub(4))  error, 2 are uninitialized so they need to be initialized in function call
print(sumsub(1,2,3,4))
