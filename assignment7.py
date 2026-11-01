# ==========================================
# Part 1: Working with Tuples
# ==========================================

# 1. Create a tuple named days containing the seven days of the week
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# 2. Display the entire tuple
print("Days tuple:", days)

# 3. Display elements using indexing
print("First day:", days[0])
print("Fourth day:", days[3])
print("Last day:", days[-1])

# 4. Display total number of elements using len()
print("Total number of days:", len(days))

# 5. Use a for loop to display each day on a separate line
print("\nDays of the week:")
for day in days:
    print(day)

# 6. Check whether "Monday" exists in the tuple
if "Monday" in days:
    print("\nMonday is in the tuple.")
else:
    print("\nMonday is not in the tuple.")

# 7. Attempting to change an element in a tuple:
# days[0] = "Holiday"
# Explanation: Tuples are immutable in Python. Once created, their elements cannot be changed,
# added, or removed. Attempting to modify an item causes a TypeError: 'tuple' object does not support item assignment.


# ==========================================
# Part 2: Working with Sets
# ==========================================

# 1. Create a set named colors
colors = {"Red", "Blue", "Green", "Yellow"}

# 2. Display the entire set
print("\nInitial colors set:", colors)

# 3. Add "Purple" using add()
colors.add("Purple")
print("After adding Purple:", colors)

# 4. Remove "Yellow" using remove()
colors.remove("Yellow")
print("After removing Yellow:", colors)

# 5. Ask user for favorite color and add it to the set
favorite_color = input("\nEnter your favorite color: ")
colors.add(favorite_color)

# 6. Use a for loop to display each color on a separate line
print("\nColors in the set:")
for color in colors:
    print(color)

# 7. Display the total number of unique colors using len()
print("Total number of unique colors:", len(colors))

# 8. Create set1 and set2
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)

# 9. Perform set operations
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))