# --------------------------------------------------------------------------------------------------
# ------------ print(object) and with replacement operator ------------------------------
# --------------------------------------------------------------------------------------------------


# ---------------------------------------------------
# Case-1 : We can pass any type of object as argument, no problem with print statement
# ---------------------------------------------------

l = [10,20,30,40]
print(l)
print(type(l))
t = (10,20,30,40)
print(t)
print(type(t))

# ---------------------------------------------------
# Case-2 : print() with replacement operator
# ---------------------------------------------------

name = "Ashish"
salary = "50000"
friend = "Shubham"
print("Hi, My name is {}, working at {} current pay, and my best friend is {}".format(name,salary,friend))

# Example through indexing
print("Hi, My name is {0}, working at {1} current pay, and my best friend is {2}".format(name,salary,friend))
print("Hi, My name is {0}, my best friend is {2}, and I am currently working at {1} current pay".format(name,salary,friend))

# giving a variable
print("Hi, My name is {n}, working at {s} current pay, and my best friend is {f}".format(n=name,s=salary,f=friend))


a,b,c,d = 10,20,30,40
print("a={}, b={}, c={}, d={}".format(a,b,c,d))





