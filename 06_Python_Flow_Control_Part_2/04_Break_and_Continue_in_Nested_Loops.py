# -----------------------------------------------------------------------------
# ------------ Break and Continue in Nested Loops ---------------
# -----------------------------------------------------------------------------

for i in range(3):
    for j in range(3):
        if i==j:
            break
        print(f"i=>{i} and j=>{j}")


for i in range(3):
    for j in range(3):
        if i==j:
            continue
        print(f"i=>{i} and j=>{j}")