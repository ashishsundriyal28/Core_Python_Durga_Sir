# Range
# Imp points : 
# 1. Sequence important
# 2. 3 forms
# 3. order, index, slice
# 4. Immutable

import os
# Clearing the Screen
os.system('cls')


r = range(10)
print(type(r))
print(r)

# if we want to get values inside range values
# use loops
for i in r:
    print(i, end="->")

# Form 1 : range(n) => from 0 to n-1
r = range(10)
for i in r:
    print(i, end="->")
print()

# Form 2 : range(begin, end) => from begin to end-1
r = range(1,10)
for i in r:
    print(i, end="->")

print()
print()
print()
print()
    
# Form 3 : range(begin, end, increment/decrement) => from begin to end-1 with increment/decrement steps
r = range(1,21,3)   #1,4,7,10....
for i in r:
    print(i, end="->")


print()
print()
print()
print()

r = range(20,1,-2)  #20,18,16,14...
for i in r:
    print(i, end="->")


print()
print()


# indexing concept is applicable in range
r = range(10,21)
print(r[0])
print(r[-1])

print()
print()
print()


# slicing concept is applicable in range
r = range(10,21)
print(r[1:5])


# range object is immutable => can't change its objects
r = range(10,21)
r[1] = 100000
print(r)        #TypeError