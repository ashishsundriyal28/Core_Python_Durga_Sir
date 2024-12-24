# -----------------------------------------------------------------------------
# ------------ Continue Statement ---------------
# -----------------------------------------------------------------------------
# To skip the current iterationa nd continue from the next iteration


# EXAMPLE : 

for i in range(10):
    if i%2==0:
        continue
    else:
        print("i=>",i)
print("outside loop")

cart=[10,20,30,600,70,80]
for item in cart:
    if item>500:
        print("To place this order, insurance is required")
        continue
    print('Processing Item:',item)


l=[10,20,0,5,0,30]
for x in l:
    if x == 0:
        print('Hello Stupid,How we can divide with zero')
        continue
    print('100/{} = {}'.format(x,100/x))