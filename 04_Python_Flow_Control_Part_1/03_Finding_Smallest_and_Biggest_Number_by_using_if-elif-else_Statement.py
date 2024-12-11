# --------------------------------------------------------------------------------------------------
# ---------- Finding Smallest and Biggest Number by using if-elif-else Statement -------------------
# --------------------------------------------------------------------------------------------------

'''
# Biggest Number
a=int(input( 'Enter First Number: ') )
b=int(input('Enter Second Number:'))
if a>b:
    print('Biggest Number:',a)
else:
    print('Biggest Number: ',b)
'''

'''
# Smallest Number
a=int(input( 'Enter First Number: ') )
b=int(input('Enter Second Number:'))
if a<b:
    print('Smallest Number:',a)
else:
    print('Smallest Number: ',b)
'''

# Biggest Number of 3 numbers
a=int(input('Enter First Number:'))
b=int(input('Enter Second Number:'))
c=int(input('Enter Third Number:'))
if a>b and a>c:
    print('Biggest Number:',a)
elif b>c:
    print('Biggest Number:',b)
else:
    print('Biggest Number:',c)



# a number is between 1 and 100
n=int(input('Enter Number :'))
if n>=1 and n<=100 :
    print(f'{n} is between 1 and 100')
else:
    print(f'{n} is not between 1 and 100')


