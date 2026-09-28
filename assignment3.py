# Programming Assignment 3.1: Operators and Expressions in Python

# Step 1: Prompt the user for three inputs (initially stored as strings)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

# Step 2: Print the value and data type before conversion
print("\n--- Initial Input Values and Types ---")
print(f"The value of num1 is {num1}, and it is of the type {type(num1)}.")
print(f"The value of num2 is {num2}, and it is of the type {type(num2)}.")
print(f"The value of num3 is {num3}, and it is of the type {type(num3)}.")

# Step 3: Convert inputs to float (allows decimals as well as whole numbers)
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

print("\n--- Converted Data Types ---")
print(f"num1 converted type: {type(num1)}")
print(f"num2 converted type: {type(num2)}")
print(f"num3 converted type: {type(num3)}")

# Step 4: Basic Arithmetic Operations (+, -, *, /)
print("\n--- Arithmetic Operations ---")
print(f"The sum of num1 and num2 is {num1 + num2}.")
print(f"The difference of num1 and num2 (num1 - num2) is {num1 - num2}.")
print(f"The product of num1 and num2 is {num1 * num2}.")
if num2 != 0:
    print(f"The quotient of num1 divided by num2 is {num1 / num2}.")
else:
    print("Cannot divide by zero for num1 / num2.")

# Step 5: Order of Operations with and without Parentheses
print("\n--- Order of Operations ---")
result = num1 + num2 * num3
print(f"Expression without parentheses (num1 + num2 * num3): {result}")

result2 = (num1 + num2) * num3
print(f"Expression with parentheses ((num1 + num2) * num3): {result2}")

# Step 6: Comparison Operators (Displaying True or False)
print("\n--- Comparisons ---")
print(f"Is num1 greater than num2? {num1 > num2}")
print(f"Is num2 equal to num3? {num2 == num3}")
print(f"Is num3 less than or equal to num1? {num3 <= num1}")