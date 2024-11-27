# --------------------------------------------------------------------------------------------------
# ------------ Demo Program 2 - Read Input data from the user ----------------------
# --------------------------------------------------------------------------------------------------
# Ques.: Write a program to read employee data from the keyboard and print the data
# --------------------------------------------------------------------------------------------------

eno = int(input("Enter employee number : "))
ename = input("Enter name : ")
esal = float(input("Enter salary : "))
eaddress = input("Enter address : ")
# but here is a logical problem , if we provide any type of string inside the emarried part
# it will give the result as TRUE even if we write as FALSE
# So the better way to handle is, instead of *bool*, we should use *eval*
# String to bool function conversion/handling, instead of using *bool*, should always use *eval*
# emarried = bool(input("Employee Married?[True/False]"))
emarried = eval(input("Employee Married?[True/False]"))

print(eno)
print(ename)
print(esal)
print(eaddress)
print(emarried)

