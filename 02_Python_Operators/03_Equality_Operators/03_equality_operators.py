# Equality operators
# == => Equal to, != => not equal to

print(10 == 10)
print(10 == 10.0)
print(10 != 20)
print('ashish'=='ashish')
print(10 == 'ashish')
print(10 == '10')

# Chaining of equality operators
# even if one wrong, result is wrong
print(10 == 10 == 10 == 40)


# Difference between '==' and 'is' operator

# '==' is meant for content comparison
# 'is' is meant for address/reference comparison

l1 = [10,20,30]
l2 = [10,20,30]
# l3 and l1. now points to same object
l3 = l1
print("is l1==l2 => ", l1==l2)
print("is l1 is l2 => ", l1 is l2)
print("is l3 is l1 => ", l3 is l1)