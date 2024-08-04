import os
os.system('cls')

# 1. "+" for string (concatenation) => str+str
# 2. "*" for String => String multiplication operator
#                   => String repetation operator
#                                                   => int * str OR str * int


#  *-> for strings => repetations that much times
print("ashish "*3)
print(3*" ashish ")
# print("durga"*"soft") #typeerror
# print("durga"*"3") #typeerror
print("durga"*int("3"))



# 3. x/0, x//0, x%0 => ZeroDivisionError
# print(10/0)
# print(10.0/0)
# print(10//0)
# print(10.0//0)
# print(10%0)
# print(10.0%0)


print("ashish"*True)
print("=>", "ashish"*False)