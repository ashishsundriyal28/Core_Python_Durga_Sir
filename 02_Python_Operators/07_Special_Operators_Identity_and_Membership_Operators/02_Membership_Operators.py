# ===============================================================================
# SPECIAL OPERATORS

# 1. IDENTITY OPERATORS
# 2. MEMBERSHIP OPERATORS
# ===============================================================================


# ===============================================================================
# ---------- 2. Membership Operators --------------
# ===============================================================================

#  => in
#  => not in

# a in sequence      => TRUE if a is present in sequence (can be string, list, tuple, etc.)
# a not in sequence  => TRUE if a is not present in sequence (can be string, list, tuple, etc.)


s = "hello learning python is very easy"
print('h' in s)
print('d' in s)
print('d' not in s)
# string passed to check is case-sensitive
print('python' in s)
print('Python' in s)

l = ["sunny", "bunny", "chinny", "vinny"]
print("sunny" in l)
print("punny" in l)



