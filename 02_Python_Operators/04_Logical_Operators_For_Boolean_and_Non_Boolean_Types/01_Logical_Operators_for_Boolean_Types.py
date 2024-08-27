# Logical Operators for boolean types

# and, or , not

# For Boolean Types

# and => return True if both arguments are true

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("----------------------------------------------------")
# or => return True if one of the two arguments is true

print(True or True)
print(True or False)
print(False or True)
print(False or False)


print("----------------------------------------------------")
# not => return opposite of arguments

print(not True)
print(not False)




username = input("Enter username : ")
password = input("Enter password : ")

if username == 'ashish' and password == 'ashish':
    print("VALID USER")
else:
    print("INVALID USER")