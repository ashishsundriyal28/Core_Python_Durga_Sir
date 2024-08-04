# Integral Values
# (Whole Numbers)

t=5
print(type(t))

# Python has only two data types for int type
# 1. long -> for large values (only available in python2)
# 2. int -> for comparitively small values


# We can represent int values in the following ways
# 1) Decimal form

a = 1111
print(a)

# 2) Binary form => "PREFIX" = zero b `combo of 1&0`

a = 0b1111  #=> this notation converst into decimal then stores the data
print(a)    #=> directly gives the decimal convert ans

# 3) Octal form => "PREFIX" = zero *small o OR CAPITAL O * `combo of 0to7`

a = 0o123  #=> this notation converst into decimal then stores the data
print("OCTAL ka DECIMAL ans = ",a)    #=> directly gives the decimal convert ans


# 4) Hexa decimal form => "PREFIX" = zero *small x OR CAPITAL X * `combo of 0to9 and A to E`
a = 0X10
print(a)

a = 0Xface
print(a)