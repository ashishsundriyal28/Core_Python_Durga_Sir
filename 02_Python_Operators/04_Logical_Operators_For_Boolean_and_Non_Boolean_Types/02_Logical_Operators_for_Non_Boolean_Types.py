# Logical Operators for non-boolean types

# and, or , not

# 0 means False
# non-zero means True
# empty string, list, set, tuple, dict => False

# 1. x and y => Result is x or y but not boolean type
# If x evaluates to False then result is x
# If x evaluates to True then result is y
print(0 and 20)
print(10 and 20)
print("durga" and "soft")
print("" and "soft")



# 2. x or y => Result is x or y but not boolean type
# If x evaluates to False then result is y
# If x evaluates to True then result is x
print(0 or 20)
print(10 or 20)
print("durga" or "soft")
print("" or "soft")


# 2. not x => Result is always boolean
print(not 0)
print(not 10)
print(not "durga")
print(not "")