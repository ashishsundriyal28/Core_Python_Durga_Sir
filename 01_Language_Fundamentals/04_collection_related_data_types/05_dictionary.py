# Dictionary => elements as Key-Value pairs
# curly brackets
# {name:"ashish", rollno:101}
# duplicate keys are not allowed but duplicate values are allowed
# heterogenous objects allowed
# mutable
# indexing and slicing is not possible




import os
# Clearing the Screen
os.system('cls')


d = {100:"ashish", 200:"sunny", 300:"chinny"}
print(type(d))
print(d)

# order is not imp while adding
d = {}
# d[key] = value
d[100] = "ashish"
d[200] = "sunny"
d[300] = "chinny"
print(d)


d[100] = "sunny"
print(d)