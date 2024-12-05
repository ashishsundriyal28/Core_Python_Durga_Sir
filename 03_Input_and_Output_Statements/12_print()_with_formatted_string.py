# --------------------------------------------------------------------------------------------------
# ------------ 12_print()_with_formatted_string ------------------------------
# --------------------------------------------------------------------------------------------------


# %i => signed integer
# %d => signed decimal
# %f => float
# %s => string, any other objects like list,set etc

a=10
b=20
c=30
print("a=%d, b=%d, c=%d" %(a,b,c))

name="Ashish"
marks = [10,20,30,40]
print("Hello %s, your marks list is %s" %(name,marks))

price=70.56789
print("Price = {}".format(price))
print("Price = %f" %price)
print("Price = %.2f" %price)