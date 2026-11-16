# Function definitions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Main program
print("--- Math Operations Program ---")

# Step 3: Prompt user for two numbers and convert to float
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 4: Call each function and display results
print("\n--- Results ---")
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")