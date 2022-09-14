# index 01234567890123  ..positive indexing
parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])
#negative indexing  43210987654321(negative)
#parrot=............Norwegian Blue
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
#or
print()
print(parrot[-11+14])
print(parrot[-10+14])
print(parrot[-5+14])
print(parrot[-11+14])
print(parrot[-8+14])
print(parrot[-6+14])
#Slicing
print()
print(parrot[0:6])
print(parrot[3:5])
print(parrot[:6])
print(parrot[10:])
print(parrot[:9])
print(parrot[10:])
print(parrot[:6] + parrot[6:])
print(parrot[:])
print()
#negative slicing(Norwegian Blue)
print(parrot[:-8])
print(parrot[-11:-9])
print(parrot[-4:-1])
print(parrot[-4:0])#will only print if we go from left to right else prints nothing(blank line)
print(parrot[-4:])
print(parrot[-14:-5]+parrot[-4:])
print(parrot[-14:-5]+parrot[-5:])
print()

#step in slicing
alpha="abcdefghijklmnopqrstuvwxyz"
print(alpha[::3])
phone="9937059497"
print(phone[::2])
print(alpha[25::-1]) #Imp
print(alpha[::])
print(alpha[::-1])
print(alpha[::1])
print(alpha[25::1])
print(alpha[25:])
print(alpha[25:-1:-1])#Imp(start and stop is same)
print(alpha[0:20:-1])  #in negative step slicing start value must be greater than stop value
print(alpha[-10:-13:-1])
alpha1=""
print(alpha1[:2]) #It shows no error, simply we will get a blank line
print(alpha1[0]) #It will show error-string index out of range