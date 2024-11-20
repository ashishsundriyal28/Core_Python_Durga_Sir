# ===============================================================================
# ----------------- Mathematical Functions from Math Module ---------------------
# ===============================================================================

# What is a module ? 
# Any group of class, functions, variables saved as a *.py file
# such type of python file is called module

import dmath

dmath.add(10,20)
dmath.product(10,20)


# If multiple module have same function
# Most recent one will be used automatically
def f1():
    print("f1 old")
def f1():
    print("f1 new")

f1()