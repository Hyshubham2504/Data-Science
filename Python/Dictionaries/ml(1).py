a=10
b=5
print(a+b, a-b, a**b, a*b, a/b, a//b, a%b)
import sys
print(sys.version)
print(5 or 6, 5 and 6, 0 and 5, 5 and 0, 0 or 6, 6 or 0)
g,h=float(input("enter a float number")), int(input("enter an integer"))
# by default python return string i.e why mentioned float
print(g,h)
# d=input("name").split(' ')
# print(d[0])
# print(d[1])
# print(d[2])
# print(d[3])
# print(d[4])
# d,m,y=input("date").split('/')
# print(d,m,y)
# multiline comment
'''
hello shubham
itachi
ronaldo
'''
print(__doc__)
if False-True:
    print("hello")
for i in range(100,1,-1):
    print(i)
for a in range(10):
    a=a+1
    if a%3:
        continue
    print(a)


