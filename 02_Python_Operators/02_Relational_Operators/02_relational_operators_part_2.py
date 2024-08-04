import os
os.system('cls')

print(True>False)
print(True>=False)
print(True<False)
print(True<=False)

# TypeError
# print(10<'ashish')

print("*******************************************\n")

a = 10
b = 20

if a>b:
    print("a is greater that b")
else:
    print("a is smaller that b")


print("*******************************************\n")
print("Chaining of relational operators\n")
print("If one is wrong whole becomes false")
print(10<20)
print(10<20<30)
print(10<20<30<40)
print(10<20<30<40>50)
