# Fundamental data types vs. Immutability
# 5 fundamental data types (int, float,complex,bool,string) 
# but, immutability applies to only 4 not on complex

a = 10
b = 10
print(a is b)

a = 10.5
b = 10.5
print(a is b)

a = True
b = True
print(a is b)

a = "Ashish"
b = "Ashish"
print(a is b)

a = 10+20j
b = 10+20j
print(a is b)