# Type casting functions
# 5 functions

'''
1. int()
2. float()
3. complex()
4. bool()
5. str()
'''

# ======================= 1. other types to int() ===============================================
# to convert from other types to int types

# ------------> float() to int()
a = int(10.989)
print(a)

# ------------> float() to int() => complex number can't be converted into int types
# a = int(10+20j)
# print(a)

# ------------> bool to int()
a = int(True)
print(a)


# ------------> string to int() => only when string contains integral values that too in base-10
a = int("10")
print(a)

# b = int("10.2") #error
# c = int("0B111")    #error
