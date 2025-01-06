# -----------------------------------------------------------------------------
# ------------ Del Statement ---------------
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Purpose of del Keyword:
# -----------------------------------------------------------------------------

# del is used to delete variables in Python.
# Deleting a variable frees memory and makes the corresponding object eligible for garbage collection, 
# which improves memory usage and reduces the risk of memory issues in programs.

# -----------------------------------------------------------------------------
# Behavior After Deleting a Variable:
# -----------------------------------------------------------------------------
# After using del, you cannot access the variable anymore.
# Attempting to access a deleted variable results in a NameError.

x = 10 
print(x)
del x
# print(x)    # NameError: name 'x' is not defined

# -----------------------------------------------------------------------------
# Deleting Reference Variables:
# -----------------------------------------------------------------------------

# If multiple variables point to the same object, deleting one reference does not delete the object.
# The object is still accessible through other references.
# To delete the object, all references to it must be deleted.
# You can delete multiple reference variables in one statement using del var1, var2.


s1 = "ashish"
s2=s1
s3=s1
print(s1 , s2 , s3)

del s1, s2
print(s3)


# -----------------------------------------------------------------------------
# del and Immutable Objects:
# -----------------------------------------------------------------------------

# You can delete a reference variable that points to an immutable object (like a string or tuple).
# You cannot delete elements inside immutable objects using del, because these objects cannot be modified.
# Example: del s[0] will raise an error for a string because strings are immutable.

# del s3[0] # TypeError: 'str' object doesn't support item deletion


# -----------------------------------------------------------------------------
# del vs. None:
# -----------------------------------------------------------------------------

# del x: Deletes the variable x. You cannot access x after deletion. This makes the object eligible for garbage collection.
# x = None: Assigns None to x, but the variable x still exists. The object previously referenced by x becomes eligible for garbage collection, but you can still access x (which will now hold None).

y = 10
print(y)

# del y # gives error

y = None
print(y)
