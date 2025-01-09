# -----------------------------------------------------------------------------
# ------------ Prime Numbers and Questions ---------------
# -----------------------------------------------------------------------------

# A +ve integer greator than 1 which has no other factors except than 1 and that number itself.

# -----------------------------------------------------------------------------
# Ques 1 : WAP to check whether a given number is prime or not
# -----------------------------------------------------------------------------
'''
n = int(input("Enter number : "))

if n<=1:
    print("Less than one")

else:
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime = False
            break
    
    if is_prime == True:
        print("Prime")
    else:
        print("NP")
'''


# ******************************************************
# Optimised verison : to reduce the no of iterations
# ******************************************************


'''
if n<=1:
    print("Less than one")

else:
    is_prime = True
    for i in range(2,n//2 + 1):
        if n%i==0:
            is_prime = False
            break
    
    if is_prime == True:
        print("Prime")
    else:
        print("NP")
'''




# --------------------------------------------------------------------------------------------
# Ques 2 : WAP to generate prime numbers which are less than or equal the given number
# --------------------------------------------------------------------------------------------


'''
n = int(input("Enter number : "))
n1=2

while n1<=n:
    # code to check if n1 is prime or not
    is_prime=True
    for i in range(2,n1//2 + 1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("n1 = ", n1)
    n1=n1+1
'''






# --------------------------------------------------------------------------------------------
# Ques 3 : WAP to generate first n prime numbers 
# --------------------------------------------------------------------------------------------

n = int(input("Enter number : "))
count=0
n1=2

while True:
    # code to check if n1 is prime or not
    is_prime=True
    for i in range(2,n1//2 + 1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("n1 = ", n1)
        count = count+1
    if count == n:
        break
    n1=n1+1






































