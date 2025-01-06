# -----------------------------------------------------------------------------
# ------------ Pass Statement ---------------
# -----------------------------------------------------------------------------

# pass is a Python-specific keyword used to represent an empty statement or block.
# It is not available in languages like C, C++, or Java.

# -----------------------------------------------------------------------------
# Purpose of the Pass Statement:
# -----------------------------------------------------------------------------
# Empty Block Placeholder: Used when a block of code is required but you don’t know the implementation yet.
# Future Code Placeholder: It allows you to write code skeletons and later replace pass with actual code.

# -----------------------------------------------------------------------------
# Key Use Cases:

#  => Functions with No Implementation: If you define a function but don’t know what it should do yet, use pass inside it.

def my_function():
    pass

# => Classes with No Implementation: If you want to define a class but don’t know what it should contain yet, use pass inside it.

class MyClass:
    pass
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Handling Syntax Errors:
# -----------------------------------------------------------------------------
#  => In Python, if a block is expected (like for a function or class body), but it’s left empty, you will get a syntax error.
#  => To avoid this error, use pass to fulfill the requirement for an empty block.


# It also works with conditional statements like if-else

# num = int(input("Enter number : "))
# if num>=35:
#     print("success")
# else:
#     pass


# -----------------------------------------------------------------------------
# Where we can use pass statement?
# Syntactically block is required, but I don't know implementation of that block. 
# Then we can implement that empty block with a pass statement.
# Pass statement acts as empty block pass statement acts as a place holder for future implementation.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Abstract Methods:
# -----------------------------------------------------------------------------
# pass is used in abstract methods (methods that are declared but not implemented).
# These methods are intended to be implemented by child classes.

from abc import ABC, abstractmethod
class Loan(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass
class HomeLoan(Loan):
    def get_interest_rate(self):
        return 8
class VehicleLoan(Loan):
    def get_interest_rate(self):
        return 11

h = HomeLoan()
print(h.get_interest_rate())



# -----------------------------------------------------------------------------
# Minimal Functions & Classes:
# -----------------------------------------------------------------------------
# Use pass to create minimal classes and minimal functions with no body.

# Example of a minimal function/method:
def minimal_function():
    pass

# Example of a minimal class:    
class MinimalClass:
    pass