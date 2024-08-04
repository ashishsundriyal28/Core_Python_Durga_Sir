# bytes => a group of byte values
# range is only (0,255)
# immutable
# duplicate values allowed

l = [10,20,30,40]
b = bytes(l)
print(type(b))


for x in b:
    print(x)

# 1. values only from 0 to 255
l = [10,20,255]
b = bytes(l)
print(b)


# l = [10,20,30,40]
# b = bytes(l)
# print(b[0])
# b[0] = 77   # not possible
# print(b[0]) #error



import os
# Clearing the Screen
os.system('cls')


# bytearray => a group of byte values
# range is only (0,255)
# duplicate values allowed
# => mutable

l = [10,20,30,40]
b = bytearray(l)
print(type(b))
print(b[0])
b[0] = 77
print(b[0])

for x in b:
    print(x)