#Basic Calculator for performing simple operations
print("Python Calculator")
print("Which function do you want to proceed: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num = input("Enter the function: ")      #Selecting the Operation
val = float(input("Enter the first number: "))    #Entering the first value
val1 = float(input("Enter the second number: "))  #Entering the second value

#Operations performed based on the selection of function
if num == "1":
    print(val + val1)
elif num == "2":
    print(val - val1)
elif num == "3":
    print(val * val1)
else:
    print(val / val1)
