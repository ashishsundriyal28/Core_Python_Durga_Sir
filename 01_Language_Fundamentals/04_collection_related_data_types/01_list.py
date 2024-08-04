# List = square brackets 
# to represent group of objects as single entity where allowed duplicate values
# [10,20,30]

# 1. Order preserved (imp)
# 2. duplicate objects are allowed
# 3. [] => square brackets
# 4. Heterogenous Objects
# 5. Indexing and slicing concept applicable
# 6. Growable in nature
# 7. Mutable

l = [10, "Ashish", 20, 10, 30]
print(type(l))
print(l)
print(l[0])
print(l[-1])

# gives list of elements from 1 to 4-1=3rd index
print(l[1:4])


l = []

l.append(10)
l.append(20)
l.append(30)
l.append(40)
print(l)
l.remove(30)
print(l)

l[0] = 7777
print(l)