# If the operator works on only one operand -> its called unary operator
# Example : ~a (~ is an unary operator)

# If the operator works on two operands -> its called binary operator
# Example : a + b (+ is binary operator)


# ===============================================================================
# When there are three operands, in that case ternary operators is used
# Also called Conditional operator

# SYNTAX : 
# c = first_value if condition else second_value
# ===============================================================================

a = 100
b = 20
c = 30 if a>b else 40
print(c)


# Read two values from the user and tell which one is minimum
a = int(input("Enter First Number  : "))
b = int(input("Enter Second Number  : "))
c = a if a<b else b
print(c)
