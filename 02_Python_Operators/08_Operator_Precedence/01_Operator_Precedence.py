# ===============================================================================
# ---------------------------- Operator Precedence ------------------------------
# ===============================================================================
print(10+2*3)
print((10+2)*3)
print("----------------------------------")
a = 30
b = 20
c = 10
d = 5

# Example 1
# Goes like first parantheses => (a+b) = 30+20=50
# => 50*10/5
# Both multiplication and division have the same precedence level
# Therefore, 50*10 = 500, then 500/5 = 100.0 (division gives floating point value)
print((a+b)*c/d)

# Example 2
# Goes like first parantheses => (a+b) = 30+20=50
# Then Second parantheses => (c/d) = 10/5=2.0
# Then final step => 50*2.0 = 100.0
print((a+b)*(c/d))

# Example 3
# Goes like first parantheses => (b+c) = 20*10=200
# Then => (a+200/5) Higher precedence is division
# Therefore, 200/5 = 40.0
# a+40.0 => 30 + 40.0 = 70.0
print(a+(b*c)/d)