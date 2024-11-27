# Python power is its modules (in-built or third-party)
# Eg. : math, ranodom, time, threading etc


'''
# Eg. : various things available inside the math module
import math
# gives complete *list* of variables/functions inside math module
print(dir(math))

print(math.sqrt(16))    # return in float
print(math.pi)

print(math.floor(3.9))
print(math.ceil(3.9))
print(math.pow(3,2))
'''
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
'''
# We don't need to write the complete module name everytime
# We can give alias to the modules
# If given alias name, then we cannot mention the complete name of the module
# otherwise it will give errors

import math as m
# Eg : print(math.floor(3.9)) => This won't work as we define alias name
print(m.sqrt(16))    # return in float
print(m.pi)
print(m.floor(3.9))
print(m.ceil(3.9))
print(m.pow(3,2))
'''
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
'''
# If we don't want to write module name everytime
# We can just import only those functions which are to be 
# -------------------------------------------
# only these 2 imports works
from math import sqrt,pi
# all imports works without mentioning module name everytime
# from math import *
print(sqrt(16))
print(pi)
'''
# -------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# We can also give alias to the functions 
# -------------------------------------------
from math import sqrt as s,pi as p
print(s(16))
print(p)