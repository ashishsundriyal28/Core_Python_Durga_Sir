# --------------------------------------------------------------------------------------------------
# ----------------------- AAPLICATIONS : For loop ------------------------------------------
# --------------------------------------------------------------------------------------------------

# range(n)  => 0 to n-1
# range(m,n)  => m to n-1
# range(m,n,increment/decrement)  => m to n-1 with increment step values

# print no 1 to 10
# for x in range(1,11):
#     print(x)

# for x in range(21):
#     if(x%2==0):
#         print(x)

# for x in range(1,21,2):
#     print(x)

# # 10 to 1 in decresing order 
# for x in range(10,0,-1):
#     print(x)



# to print sum of numbers of a list
list = eval(input("Enter list of numbers : "))
# s=0
# for x in list:
#     s = s+x
# print(sum)
print(sum(list))

