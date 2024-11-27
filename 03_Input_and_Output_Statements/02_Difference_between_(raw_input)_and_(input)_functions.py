# --------------------------------------------------------------------------------------------------
# --------------- Difference between raw_input() vs input() ----------------------------------------
# --------------------------------------------------------------------------------------------------

# both are used to take input from the user
# Python 2.x funtion

'''
# BELOW are Python 2.x functions, won't work in python 3.x
# 1. raw_input()
# used to read the data provided by the end user
# PROBLEM: The return type of raw_input() is, it is always going to provide in the form of string only. Even if we provide integer, it converts it them into string, we have to do type-casting to get th eint back.

x = raw_input("Enter some value : ")
print(type(x))
y = int(x)
print(type(y))

# 2. input()
# ADVANTAGE: The return type of input() is, always the type provided by the user.

x = input("Enter some value : ")
print(type(x))
y = int(x)
print(type(y))
'''

# Python 2.x and 3.x both used to have the input() method
# but the input() method in python 3.x is not like python 2.x
# input() of python 3.x is same like raw_input of python 2.x
# that means, return type of input() is always going to provide in the form of string only.
x = input("Enter some value : ")
print(type(x))
y = int(x)
print(type(y))



