# --------------------------------------------------------------------------------------------------
# ----------------------- Command Line Arguments ----------------------------------------------
# ------------------------------- Part 1 ----------------------------------------------
# --------------------------------------------------------------------------------------------------
from sys import argv

print(type(argv))
print(argv[0])
print(argv[1])
print(argv[2])
print(argv[3])
print(argv)


# --------------------------------------------------------------------------------------------------
# Program to print command line arguments
# --------------------------------------------------------------------------------------------------
print("The number of command line arguments : ", len(argv))
print("The list of command line arguments : ", argv)
print("The command line arguments one by one : ")
for x in argv:
    print(x)