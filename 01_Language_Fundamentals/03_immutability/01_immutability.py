# Fundamental data types vs Immutability
# The fundamental data types are : int, float, complex, bool, str

# once we create an object, we can not perform any changes in that object.
# If we are trying to perfrom any changes, with those changes, 
# a new object will be created

x = 10
print(id(x))

x = x + 1
print(id(x))



x = 10
y = x
print(id(x))
print(id(y))

y = y + 1
print(id(y))