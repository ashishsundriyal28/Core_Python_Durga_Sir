# Bitwise Operators

# & => Bitwise and
# | => Bitwise or
# ^ => Bitwise X-OR
# ~ => Bitwise complement operator
# << => Bitwise Left-Shift operator
# >> => Bitwise Right-Shift operator

# we can apply bitwise operators only for
# int and bool type

# print(10.5&20.5)
# print('durga' & 'durga')

print(10 & 20)
print("-------------------------------------------")
# & => If both bits are 1 then only result is 1 otherwise result is 0
# | => If atleast one bit is 1 then result is 1 otherwise result is 0
# ^ => If bits are different then only result is 1 otherwise result is 0
# ~ => bitwise complement operator
# 1 -> 0 & 0 -> 1

print(4 & 5)
# Explaination =>
# 4 -> 1 0 0
# 5 -> 1 0 1 
# -----------------
# & => 1 0 0        => 4 ans.
# -----------------
print("-------------------------------------------")


print(4 | 5)
# Explaination =>
# 4 -> 1 0 0
# 5 -> 1 0 1 
# -----------------
# | => 1 0 1        => 5 ans.
# -----------------
print("-------------------------------------------")

print(4 ^ 5)
# Explaination =>
# 4 -> 1 0 0
# 5 -> 1 0 1 
# -----------------
# ^ => 0 0 1        => 1 ans.
# -----------------
print("-------------------------------------------")