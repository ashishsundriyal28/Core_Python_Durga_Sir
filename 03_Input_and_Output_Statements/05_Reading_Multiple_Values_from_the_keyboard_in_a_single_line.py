# --------------------------------------------------------------------------------------------------
# ------------ Reading Multiple Values from the keyboard in a single line ----------------------
# --------------------------------------------------------------------------------------------------
# ------------ List comprehension concept ------------
# 1. if we just write input("Enter 2 num : ") => it will take input as '10 20'
# 2. if we do input("Enter 2 num : ").split() => it will convert '10 20' as ['10','20']
# 3. looping part for x in input()... => iterates over values 10 and 20
# 4. converting value from string to integer using int(x)
'''
a,b = [int(x) for x in input("Enter 2 num : ").split()]
print("THE SUM : ", a+b)
'''

# ------------------------ Breaking down everything ------------------------

# input type is always string
s = input("Enter 2 num : ")
print(s)
# return type of split is list
l = s.split()
print(l)
# Converting list to int type
l1 = [int(x) for x in l]
print(l1)
# Unpacking the list
a,b = l1
print(a , "<=>" , b)


# Writing a program to read 3 float values from the keyboard with , separation and print the sum
a,b,c = [float(x) for x in input("Enter 3 num : ").split(",")]
print("THE SUM : ", a+b+c)