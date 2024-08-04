# Tuple = round brackets 
# to represent group of objects as single entity where allowed duplicate values
# (10,20,30)
# same as list but immutable
# a read-only version of list


t = (10,20,30,20,10,'ashish')
print(type(t))
print(t)
print(t[0])
print(t[-1])
print(t[1:4])

# t[0] = 77777
# print(t)    #type error


t = ()  # empty tuple
print(type(t))

# single element tuple is considered as int data type
t = (10)
print(type(t))


# if you want to take a single element tuple
# take it with a comma
t = (10,)
print(type(t))  #tuple


