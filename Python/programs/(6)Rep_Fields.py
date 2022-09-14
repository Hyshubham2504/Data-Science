age=18
print("I am " + str(18) + " years old")
print("I am {0} years old".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31,"Jan","March","May","July","Aug","Oct","Dec."))
#If i dont mention the field no.s values will be inserted in order-wise
print("There are {0} days in jan, march, may, july, aug, oct, dec".format(31))
print("Jan:{2} Feb:{0} Mar:{2} Apr:{1} May:{2} Jun:{1} Jul:{2} Aug:{2} Sep:{1} Oct:{2} Nov:{1} Dec:{2}".format(28,30,31))
print("""Jan:{2} 
Feb:{0} 
Mar:{2} 
Apr:{1} 
May:{2} 
Jun:{1} 
Jul:{2} 
Aug:{2} 
Sep:{1} 
Oct:{2} 
Nov:{1} 
Dec:{2}""".format(28,30,31))
#If i dont mention field no.s I cannot use a value more than once