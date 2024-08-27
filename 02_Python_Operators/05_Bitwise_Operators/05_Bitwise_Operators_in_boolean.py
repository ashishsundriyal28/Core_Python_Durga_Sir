# &
print(True & False)

# |
print(True | False)

# ^
print(True^False)

# ~
print(~True)

# true = 1
# 1  = 0 0 0 0 . . . . 0 0 1
# ~1 = 1 1 1 1 . . . . 1 1 0   {first 1 is MSB for -ve}

#        1 1 1 . . . . 1 1 0
# -----------------------------
# 1's :  0 0 0 . . . . 0 0 1
# -----------------------------
# 2's :  0 0 0 . . . . 0 1 0
# i.e. => 2
# Final ans : -2 {-ve bcz of the MSB}


# <<
print(True << 2)
print(1 << 2)

# >>
print(True >> 2)
print(1 >> 2)