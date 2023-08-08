# Create a set
fruits_set = {"apple", "banana", "passion", "date", "", "lemon"}
new_set = {"orange", "pawpaw"}

# Find the length of the setorange
set_length = len(fruits_set)
print("Length of the set:", set_length)

# Check the data type of the set
set_type = type(fruits_set)
print("Data type of the set:", set_type)

# Accessing items in the set
for item in fruits_set:
    print(item)
    
# Add an item to the set
fruits_set.add("mango")
print(fruits_set)


# Add two sets together
combined_set = fruits_set.union(new_set)
print(combined_set)