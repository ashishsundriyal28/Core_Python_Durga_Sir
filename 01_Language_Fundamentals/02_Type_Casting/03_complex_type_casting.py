# ======================= 2. other types to complex() ===============================================
# to convert from other types to complex types

# complex type => a+bj
                # => where a = real, b = imaginary

# ================ Form-1. complex(x) ===========================
 
#       => complex(x) -> x becomes the real part

a = complex(10)
print(a)


#  can decode even binary, octal and hexadecimal form
a = complex(0XFace)
print(a)

#  can decode even float form
a = complex(10.5)
print(a)


#  can decode even boolean form
a = complex(False)
print(a)


#  can decode even string form but string should contain only int/float type
a = complex("10.5")
print(a)


a = complex("10")
print(a)



# ================ Form-2. complex(x,y) ===========================

    # => complex(x,y) => x=real, y=img part

a = complex(10,20)
print(a)

# can also handle float types
a = complex(10.5,20.6)
print(a)



# if first is string, then type error

# a = complex("10",20)
# print(a)    #TypeError: complex() can't take second arg if first is a string

