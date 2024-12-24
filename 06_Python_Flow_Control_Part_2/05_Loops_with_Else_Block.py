# -----------------------------------------------------------------------------
# ------------ Loops with Else Blocks ---------------
# -----------------------------------------------------------------------------
# If the loop is executed without any break statement, then only else part will be executed

# EXPLAINATION : 
# If break statement are not encountered inside the loop
# (If a loop successfuly completes execution without executing the break statement), 
# then only else part is going to execute.
# If break statement executes, else part will not execute

cart=[10,20,600,40,50]
for item in cart:
    if item>500:
        print("Can't place this order")
        break
    print('Processing Item:',item)
else:
    print("Congrats, All items processed successfully")



# So else a support is meaningful with a break, not meaningful with the continuous statement.
cart=[10,20,600,40,50]
for item in cart:
    if item>500:
        print("Can't place this order")
        continue
    print('Processing Item:',item)
else:
    print("Congrats, All items processed successfully")




# Repeat code for every item in sequence: for loop

# Repeat code as long as some condition is True: while loop