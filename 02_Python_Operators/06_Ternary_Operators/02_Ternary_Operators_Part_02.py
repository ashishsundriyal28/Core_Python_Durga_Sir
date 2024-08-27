# ===============================================================================
# Learning use of Nested Ternary operator

# SYNTAX : 
# c = first_value if condition else second_value
# ===============================================================================

# ===============================================================================
# Read two values from the user and tell which one is minimum
# ===============================================================================

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number  : "))
c = int(input("Enter Third Number  : "))
# This logic is perfect
min = a if a<b and a<c else b if b<c else c
print("Minimum value : ", min)

max = a if a>b and a>c else b if b>c else c
print("Maximum value : ",max)

# Below logic gives error
# min = a if a<b<c else b if b<c else c
# print("Minimum value : ", min)



# ===============================================================================
# ------------------------ EXERCISE ---------------------------------
# Read two values from the user and tell which one is minimum
# if equal print "Equal"
# if a>b print "bigger"
# if a<b print "smaller"
# ===============================================================================

a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number  : "))
# This logic is perfect
output = "equal" if a==b else "smaller" if a<b else "bigger"
print("Output : ", output)