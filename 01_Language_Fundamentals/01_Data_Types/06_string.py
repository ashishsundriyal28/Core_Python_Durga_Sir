a = "ashish"
print(type(a))


b = 'ashish'
print(type(b))

c = "a"
print(type(c))  # => str , in python there is no char type

# Triple quotes => '''string''' OR """string""""""

# Advantages

# 1. to define multi line string literals 

d = '''durga 
    software
    solutions'''
print(d)

# 2. to mention quotes(both single and double) also in the string as normal characters

e = '''ashish 'is' very "handsome"'''
print(e)


# 1. to define doc string



# 

s = "ashish"
print(s[0])
print(s[3])
# print(s[100]) ERROR
print(s[-1])


# SLICE Operator
# s[begin:end]      # from index begin to end-1
# default value of begin is 0
# default value of end is end of string
s = "abcdefghijklmnopqrstuvwxyz"
print(s[1:6])   # from index 1 to 6-1=5 , gives bcdef
print(s[:9])
print(s[1:])
print(s[:])     # => total string will be considered

# Never gives index error, if end point is not given correctly (out of range),
# then it takes last index point
print(s[20:1000000])

print(s[5:1])     # => gives empty string


s = 'ashish'
t = s[0].upper() + s[1:]     # => gives "Ashish"
print(t)
print()
t = s[:len(s)-1]+ s[-1].upper()     # => gives "ashisH"
print(t)

t = s[0].upper() + s[1:len(s)-1] + s[-1].upper()     # => gives "AshisH"
print(t)

# ============ "+ operator" ==============
# both should  be string data type
s = "durga" + "soft"
print(s)

# s = "durga" + 10
# print(s)      => gives type error


# ============ "* operator" ==============
# string repeatition operator
# one should be string and another should be integer always
# any order no problem
s = "durga" * 3
print(s)

s = 3 * "durga"
print(s)


# s = "durga" * soft
# print(s)      => gives error