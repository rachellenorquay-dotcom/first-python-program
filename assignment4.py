# Programming Assignment 4: Flow Control and Branching in Python

# Step 1: Determine if number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()

# Step 2: Determine age category - Over 18 or under
age = int(input("Enter your age: "))

if age >= 18:
    print("You are 18 or older.")
else:
    print("You are under 18.")

print()

# Step 3: Branching choice from 1 to 3 with invalid fallback
choice = int(input("Enter a number from 1 to 3: "))

if choice == 1:
    print("You picked number 1.")
elif choice == 2:
    print("You picked number 2.")
elif choice == 3:
    print("You picked number 3.")
else:
    print("Invalid selection.")