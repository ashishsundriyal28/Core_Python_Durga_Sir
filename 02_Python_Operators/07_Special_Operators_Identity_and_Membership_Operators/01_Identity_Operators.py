# ===============================================================================
# SPECIAL OPERATORS

# 1. IDENTITY OPERATORS
# 2. MEMBERSHIP OPERATORS
# ===============================================================================


# ===============================================================================
# ---------- 1. Identity Operators --------------
# ===============================================================================

#  => is
#  => is not

# r1 is r2      => TRUE if and only if both references pointing to the same object
# r1 is not r2  => TRUE if and only if both r1 and r2 are not pointing to the same object


a = 10
b = 10
print(a is b)
print(a is not b)

a = "durga"
b = "durga"
print(a is b)
print(a is not b)


# In fundamental data type object reusbility is there
# but in remaining, it's not possible (even it has same content)
l1 = [10,20,30,40]
l2 = [10,20,30,40]
# they both are pointing to diff objects
print(l1 is l2)
print(l1 is not l2)
# to confirm, you can print their ids and check
print(id(l1))
print(id(l2))
# if you want content comparison, use ==
print(l1 == l2)


