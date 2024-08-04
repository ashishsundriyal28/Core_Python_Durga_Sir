# Mutability in list
# list is mutable, in the same object, changes happens

l1 = [10,20,30,40]
l2 = l1

print(l1)
print(l2)

l1[0] = 7777

print(l1)
print(l2)


l2[1] = 8888

print(l1)
print(l2)