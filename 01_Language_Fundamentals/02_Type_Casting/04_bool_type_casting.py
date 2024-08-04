# ======================= 2. other types to float() ===============================================
# to convert from other types to int types

# 1. int to bool

a = bool(10)
print(a)

a = bool(958896456)
print(a)

a = bool(0)
print(a)



# 2. float to bool

a = bool(0.0)
print(a)

a = bool(0.000000000001)
print(a)

a = bool(-0.00000002)
print(a)



# 3. complex to bool

a = bool(0+0j)
print(a)

a = bool(1+0j)
print(a)



# 4. string to bool
# only empty string is false else is true
print(bool('True'))
print(bool('False'))
print(bool('yes'))
print(bool('no'))
print(bool(''))