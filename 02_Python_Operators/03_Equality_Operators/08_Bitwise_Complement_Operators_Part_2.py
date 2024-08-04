# Bitwise Complement Operator (~)

# Example: ~5

# Binary representation of 5:
#   5  = 0 0 0 0 0 ...... 0 1 0 1 (binary form)

# Bitwise complement (~5):
#   ~5 = 1 1 1 1 1 ...... 1 0 1 0 (binary form)

# As ~5 MSB is 1, it will be a negative number.
# The rest 31 bits should be calculated in 2's complement form.

# Rest of the 31 bits:
#                       1 1 1 1 ...... 1 0 1 0 (rest 31 bits)
# -------------------------------------------------------------
# 1's complement:       0 0 0 0 ...... 0 1 0 1
# -------------------------------------------------------------
# 2's complement:       0 0 0 0 ...... 0 1 1 0 (adding 1 to 1's complement)

# Therefore, it becomes 6 but negative as MSB is 1.

print("~5   =>   ", ~5)   # Output: -6

print("=====================================================================")
print("=====================================================================")
print("=====================================================================")


# Example: ~(-4)

# Binary representation of -4 (using 2's complement):
#  -4  = 1 1 1 1 1 ...... 1 1 0 0 (binary form)

# -ve no. are represented in 2's complement form

# Bitwise complement (~(-4)):
#  ~(-4) = 0 0 0 0 0 ...... 0 0 1 1 (binary form)

# As ~(-4) MSB is 0, it will be a positive number.

# The binary representation already represents the positive number.

# Therefore, it becomes 3 as it is positive.

print("~(-4)   =>   ", ~(-4))   # Output: 3
