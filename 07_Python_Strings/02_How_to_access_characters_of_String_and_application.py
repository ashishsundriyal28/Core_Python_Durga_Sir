# --------------------------------------------------------------------------------------------------
# ------------------------------- Python Strings --------------------------------------
# --------------------------------------------------------------------------------------------------


# ------------------------------ AGENDA -----------------------------------
# How to access characters of strings and applications


# 1. By using index

# +ve index = from left to right, starts from 0
# -ve index = from right to left, starts from -1

s = "Ashish"
print(s[0], " ", s[1])
print(s[-1], " ", s[-2])



s = "durga"
i=0
for x in s:
    print(f'''The character at +ve index {i} and -ve index {i-len(s)} is {x}''')
    i=i+1
