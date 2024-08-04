'''
Rules for Idenfiers
'''
# 1.
# Only characters allowed as identifiers
# a-z, A-Z, 0-9, _

cash=10
# Gives 10 as result

# ca$h=10   # error 


# ***********************************************************************
# 2.
# digits cannot be in start as identifiers

cash123=10
# Gives 10 as result

# 123cash=10   # error 

# ***********************************************************************
# 3. 
# Python is case-sensitive

total=10
TOTAL=20
toTaL=30


# ************************** NOTE *********************************************
# diff in _variables

# x = normal variable
# _x = protected variable
# __x = private variable
# __x__ = magic variable