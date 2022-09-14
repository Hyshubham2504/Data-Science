splitstring = "This sentence\nhas been\nsplit\nfor several times."
print(splitstring)
tabstring = "1\t\t2\t3\t4\t5"
print(tabstring)
print('The doctor said,"He\'s having \'uh\' insomnia".')
# or
print("The doctor said,\"Well, he 'uh' can do great but will sure die.\"\n'So, don't worry'")
# else
print('''The doctor said, "He's having 'uh' insomnia".''')
anothersplitstring = """Cristiano \
Ronaldo Dos \
Santos Aviero\
"""
print(anothersplitstring)
# else
splitstring2 = """Cristiano
Ronaldo "Dos"
Santos 'Aviero'
"""
print(splitstring2)
print("C:\\Users\\timbuchukal\\notes.txt")
# \U and \t \n are representing escape sequences
# can clear them by either making raw strings or escaping the backslash character
print(r"C:\Users\timbuchukal\notes.txt")
