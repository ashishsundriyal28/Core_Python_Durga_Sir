# Shift Operators

# <<  --->  Left Shift
# >>  --->  Right Shift


# ----------------------------- LEFT SHIFT ------------------------------------------------

# Example: 10 << 2

# Binary of 10:  0 0 0 0 . . . . . . . 0 1 0 1 0

# Left Shift means first two bits are cut,
# So, all the digits will be shifted two places towards the left.
# Therefore, the last two blank spaces on the right side will be filled with zeros,
# and then its decimal form is calculated.

# Binary of 10:  0 0 0 0 . . . . . . . 0 1 0 1 0
#                (cut)
#                0 0 . . . . . . . 0 1 0 1 0 0 0

# Decimal form:  0 0 0 . . . . 0 1 0 1 0 0 0  :  40

print(10 << 2)


# ----------------------------- RIGHT SHIFT ------------------------------------------------

# Right Shift means the last two bits are cut,
# So, all the digits will be shifted two places towards the right.
# Therefore, the last two bits on the left side will be empty, 
# it will be filled according to the signed bit
# If the number is positive, the leftmost empty bits are filled with 0,
# if it's negative, they are filled with 1.
# and then its decimal form is calculated.

# Binary of 10:  0 0 0 0 . . . . . . . 0 1 0 1 0
#                                           (cut)
#                0 0 0 0 . . . . . . . 0 0 0 1 0

# Decimal form:  0 0 0 0 . . . . . . . 0 0 0 1 0  :  2

print(10 >> 2)



