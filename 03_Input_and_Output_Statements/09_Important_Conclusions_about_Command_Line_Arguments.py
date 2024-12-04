# --------------------------------------------------------------------------------------------------
# --------------- IMPORTANT CONCLUSIONS ABOUT COMMAND LINE ARGUMENTS -------------------------------
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# CASE-1 :  If there is space between command line arguments, then use double-quotes
# --------------------------------------------------------------------------------------------------
from sys import argv
print(argv[1])
# py .\03_Input_and_Output_Statements\09_Important_Conclusions_about_Command_Line_Arguments.py Ashish Sundriyal
# Input : Ashish Sundriyal, Output : Ashish

# if we want complete string, enclose it in double quotes 
# We should strictly use double-quotes

# py .\03_Input_and_Output_Statements\09_Important_Conclusions_about_Command_Line_Arguments.py "Ashish Sundriyal"
# Input : Ashish Sundriyal, Output : Ashish Sundriyal


# --------------------------------------------------------------------------------------------------
# CASE-2 :  Concatenation of command line arguments
# --------------------------------------------------------------------------------------------------
from sys import argv
print(argv[1]+argv[2])  # INPUT: 10 20, OUTPUT: 1020
# As index items are as strings, there will be string concatenation

# If you want mathematical operation, type-cast it into int
print(int(argv[1])+int(argv[2]))  # INPUT: 10 20, OUTPUT: 30




# --------------------------------------------------------------------------------------------------
# CASE-3 :  Index Error in Command-Line arguments
# --------------------------------------------------------------------------------------------------
from sys import argv
print(argv[100]) 
# OUTPUT : IndexError: list index out of range


