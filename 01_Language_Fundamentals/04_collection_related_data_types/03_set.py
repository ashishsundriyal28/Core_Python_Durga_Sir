# Set = curly brackets
# {10,20,30}

# 1. Order not required
# 2. duplicate objects are not allowed
# 3. {} => curly brackets
# 4. Heterogenous Objects
# 5. Growable and Mutable
# 6. list ka append function = set ka add function


# They all are equal
s1 = {1,2,3}
s2 = {3,2,1}
s3 = {1,3,2}
print(s1 == s2)


s = {10, 20, 10, 'ashish', 30}
print(s)

# print(s[0]) # error
# print(s[1:4])   #error

s = {1,2,3,4}
s.add(50)
print(s)

s.remove(2)
print(s)


# not empty set but its empty dictionary 
s = {}
print(type(s))

s = set()
print(type(s))
print(s)


