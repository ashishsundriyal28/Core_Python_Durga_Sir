# --------------------------------------------------------------------------------------------------
# ----------------------- Command Line Arguments ----------------------------------------------
# ------------------------------- Part 2 ----------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# Program to print sum of command line arguments
# --------------------------------------------------------------------------------------------------
from sys import argv

'''
# do list split from array[1], as first one is file-name
args = argv[1:]
print(args)
sum = 0
for x in args:
    sum = sum+int(x)
print(sum)
'''

# --------------------------------------------------------------------------------------------------
# File Merger application
# --------------------------------------------------------------------------------------------------
f1 = open(argv[1])
f2 = open(argv[2])
f3 = open(argv[3],'w')
for x in f1:
    f3.write(x)
for x in f2:
    f3.write(x)