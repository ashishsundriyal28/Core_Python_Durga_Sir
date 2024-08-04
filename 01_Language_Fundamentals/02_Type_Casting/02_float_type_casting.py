# ======================= 2. other types to float() ===============================================
# to convert from other types to int types

# ------------> int to float()
a = float(10)
print(a)

a = float(0B1111)
print(a)

# ------------> complex to float() => complex number can't be converted into float types
# a = float(10+20j)
# print(a)      #ERROR

# ------------> bool to float()
a = float(True)
print(a)

a = float(False)
print(a)

# ------------> string to float() => only when string contains integral values that too in base-10
a = float("10")
print(a)

b = float("15.2")
print(b)

# c = float("0XFace")    #error
