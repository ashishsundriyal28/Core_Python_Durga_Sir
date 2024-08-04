# object reusability

# if object present in memory, the new ref. variable 
# points to the same object

'''
a = 10
b = 10
c = 10
print(id(a))
print(id(b))
print(id(c))
'''

# is keyword is to check whether both the reference variable
# are pointing towards same object
a = 100.24
b = 100.24
print(a is b)
b = b + 1
print(a is b)