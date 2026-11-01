# 1. Create a list named fruits containing five different fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# 2. Display the entire list
print("All fruits:", fruits)

# 3. Display specific items using indexing
# Index 0 is the first item, index 2 is the third item, index -1 is the last item
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])

# 4. Ask the user for their favorite fruit and append it
favorite_fruit = input("Enter your favorite fruit: ")
fruits.append(favorite_fruit)

# 5. Display the updated list
print("Updated list:", fruits)

# 6. Change the second fruit (index 1) to "Mango"
fruits[1] = "Mango"
print("List after replacing the second fruit:", fruits)

# 7. Remove one fruit from the list
# Removing "Date" (or another fruit originally in the list)
fruits.remove("Date")
print("List after removing 'Date':", fruits)

# 8. Display the total number of fruits using len()
print("Total number of fruits:", len(fruits))

# 9. Use a for loop to display each fruit on a separate line
print("\nFruits printed one by one:")
for fruit in fruits:
    print(fruit)

# 10. Check whether "Apple" exists in the list
if "Apple" in fruits:
    print("\nApple is in the list.")
else:
    print("\nApple is not in the list.")

# 11. Sort the list alphabetically and display the final list
fruits.sort()
print("Final sorted list:", fruits)