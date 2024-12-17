# -----------------------------------------------------------------------------
# ------------ Break Statement ---------------
# -----------------------------------------------------------------------------
# IF YOU WANT TO USE BREAK STATEMENT, YOU SHOULD ALWAYS USE IT WITHIN THE LOOP
# OUTSIDE THE LOOP, IT WON'T WORK 
# GIVES SYNTAX ERROR
'''
i=2
if i==7:
    print("Processing is Enough, Break loop code execution........")
    break # SyntaxError: 'break' outside loop
else:
    print("i=>",i)
'''
# EXAMPLE : 

for i in range(11):
    if i==7:
        print("Processing is Enough, Break loop code execution........")
        break
    else:
        print("i=>",i)
print("outside loop")




cart=[10,20,30,600,70,80]
for item in cart:
    if item>500:
        print("To place this order, insurance is required")
        break
    print('Processing Item:',item)