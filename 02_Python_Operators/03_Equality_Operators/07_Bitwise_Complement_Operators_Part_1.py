# Bitwise Complement Operator (~)

# The most significant bit (MSB) acts as sign bit
# 0 ==> +ve number
# 1 ==> -ve number

#  +ve numbers will be represented directly in the memory
#  -ve numbers will be represented in 2's complement form

# 1's complement ==> 0 -> 1 and 1->0 (-> means "replaced with")
# 2's complement ==> 1's complement + 1

print(~4)

# Explaination :- 
# (first bit is MSB)
# 4  = 0 0 0 0 0 ...... 0 1 0 0 (binary form)
# ~4 = 1 1 1 1 1 ...... 1 0 1 1 (binary form)

# as ~4 MSB is 1, it will be a negative number
# rest 31 bits should be calculated in 2's complement form

#                   1 1 1 1 ...... 1 0 1 1 (rest 31 bits)
# -------------------------------------------------------------
# 1's complement => 0 0 0 0 ...... 0 1 0 0
# -------------------------------------------------------------
# 2's complement => 0 0 0 0 ...... 0 1 0 1 (doing +1 in 1's complement)

# therefore it makes 5 but of negative as MSB is 1

print(~4)   # output = -5
