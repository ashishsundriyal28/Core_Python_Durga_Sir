# --------------------------------------------------------------------------------------------------
# ------------ Output Statements : print() function and sep attribute ------------------------------
# --------------------------------------------------------------------------------------------------

# ---------------------------------------------------
# -------- print() function -----------
# ---------------------------------------------------

# ---------------------------------------------------
# Case-1 : print() without any arguments
# ---------------------------------------------------
print("Ashish")
print() # gives empty/blank line in between of Ashish and Sundriyal
print("Sundriyal")


# ---------------------------------------------------
# Case-2 : print(String)
# ---------------------------------------------------

# New line = \n
print("Ashish\nSundriyal") 
# OUTPUT: Ashish
#         Sundriyal

# Tab character = \t
print("Ashish\tSundriyal") # OUTPUT: Ashish  Sundriyal

# String concatenation = +
print("Ashish"+"Sundriyal") # OUTPUT: AshishSundriyal

# String multiplied no of times of a number
print(10*"Ashish") # OUTPUT: AshishAshishAshishAshishAshishAshishAshishAshishAshishAshish


# ---------------------------------------------------
# Case-3 : assign and print multiple values together
# ---------------------------------------------------
a,b,c = 10,20,30
print("Values are : ", a,b,c)
# It have automatic-spaces between them



# ---------------------------------------------------
# Case-4 : sep attribute
# ---------------------------------------------------
a,b,c,d = 10,20,30,40
print(a,b,c,d) # OUTPUT => 10 20 30 40
print(a,b,c,d, sep=":") # OUTPUT => 10:20:30:40


# ---------------------------------------------------
# Case-5 : end attribute
# ---------------------------------------------------
print("---------- WITHOUT end attribute ---------------------")
print("Hello")
print("Ashish")
print("Sundriyal")
print("---------- WITH end attribute ------------------------")
print("Hello", end=" ")
print("Ashish", end=" ")
print("Sundriyal")
print()
print("Hello", end="::")
print("Ashish", end="$$$")
print("Sundriyal")


# Continue from 9:00 end attribute

# ---------------------------------------------------
# Case-6 : sep and end attribute using together
# ---------------------------------------------------
print(10,20,30, sep=":", end="***")
print(40,50,60, sep=":")
print(70,80, sep="**", end="$$")
print(90,100)


print("Ashish"+"Sundriyal") # OUTPUT => AshishSundriyal
print("Ashish", "Sundriyal") # OUTPUT => Ashish Sundriyal


