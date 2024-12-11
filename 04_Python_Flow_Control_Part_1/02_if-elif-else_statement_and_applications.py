# --------------------------------------------------------------------------------------------------
# ----------------------- IF-ELIF-ELSE Statements ------------------------------------------
# --------------------------------------------------------------------------------------------------


# ----------------------- IF Statements ------------------------------------------
name = input("Enter name : ")
if name == "Ashish" or name == "ashish":
    print("Hello Ashish !!")
print("How are you ??")


# ----------------------- IF-ELSE Statements ------------------------------------------
# name = input("Enter name : ")
if name == "Ashish" or name == "ashish":
    print("Hello Ashish !!")
else:
    print("Hello Guest !!")
print("How are you ??")


# ----------------------- IF-ELIF-ELSE Statements ------------------------------------------
brand=input('Enter Your Favourite Brand: ')
if brand == 'KF':
    print('It is Childrens Brand')
elif brand == 'KO':
    print('It is too light')
elif brand == 'RC':
    print('It is not that much kick')
elif brand == 'FO':
    print('Buy One Get One FREE')
else:
    print("Other brands are not recommended")