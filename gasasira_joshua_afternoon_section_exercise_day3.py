#EXERCISE 1(Lists)
# 1.output 2nd item
people = ["John", "Jane", "Alice", "Bob", "Michael"]
print(people[1])

# 2.  change the value of the first item to a new value
people[0] = "Dan"
print(people)

# 3.add 6th item
people.append("Joshua")
print(people)

# 4. add 'Bathel
people.insert(2, "Bathel")
print(people)

# 5.remove 4th item
del people[3]
print(people)

# 6. last item using negative indexing
print(people[-1])

# 7.  3rd, 4th, and 5th items from a list using a range of indexes
print(people[2:5])

# 8.countries list and its copy
countries = ["USA", "Uganda", "Kenya", "TZ", "China"]
countries_copy = countries.copy()
print(countries_copy)

# 9. looping through
for country in countries:
    print(country)
    
# 10. list of animals and sort them
animals = ["ape", "elephant", "cow", "goat", "pig"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

# 11. animal with 'a'
a_animals = [animal for animal in animals if 'a' in animal]
print(a_animals)

# 12. two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Jane", "Alice"]
last_names = ["Smith", "Doe", "Johnson"]

full_names = []

for first, last in zip(first_names, last_names):
    full_names.append(first + " " + last)

print(full_names)

##########################################################################

#EXERCISE 2(Tuples)

#1. fav phone brand
x = ("samsung", 'iphone', 'tecno', 'redmi')
fav_brand=x[0]
print(fav_brand)

# 2.using negative indexing
second_last_item = x[-2]
print(second_last_item)

# 3.updating iphone to itel
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

# 4. adding huawei
x = x + ("Huawei",)
print(x)

#5. looping through
for phone in x:
    print(phone)

#6.remove first item
x = x[1:]
print(x)

#7 tuple of cities
cities = tuple(["Kampala", "Gulu", "Jinja", "Mbarara"])
print(cities)

# 8.unpack tuple 
first_city,second_city,third_city, last_city = cities
print(first_city)
print(second_city)
print(third_city)
print(last_city)

# 9.range of indexes to print the 2nd, 3rd and 4th cities
print(cities[1:4])

# 10.one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane", "Alice")
last_names = ("Smith", "Doe", "Johnson")
full_names = first_names + last_names
print(full_names)

# 11. tuple of colors and multiplyingby 3
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

# 12. counting the number of 8s
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_Number_of_8s = thistuple.count(8)
print('f{count_Number_of_8s} is the number of 8s that appear')



###########################################################################

# EXERCISE 3 (Sets)

#1. construct a setof beverages
beverages = set(["coffee", "soda", "juice"])
print(beverages)

#2. add 2 items 
beverages.add("water")
beverages.add("tea")
print(beverages)

#3. check if microwave is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")


#4. remove kettle
mySet.remove("kettle")
print(mySet)

#5. loop though set
for item in mySet:
    print(item)

#6. add items of list to set 
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)



#7  set of ages union first name
ages = {25, 30, 35}
first_names = {"John", "Jane", "Alice"}
joined_set = ages.union(first_names)
print(joined_set)


############################################################

# EXERCISE 4 (strings)
#1. string concatenation using + operator
string = 'Hello'
integer=2
concatenated_string = str(integer) + string
print(concatenated_string)

#2. removing spaces
txt = " Hello, Uganda! "
txt_without_spaces = txt.strip()
print(txt_without_spaces)

#3. to uppercase
txt_uppercase = txt.upper()
print(txt_uppercase)

#4. replace a character with another one
txt_replace = txt.replace('U','V')

#5.  range of characters in the 2nd, 3rd, and 4th positions
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

#6. correcting piece of code
x = "All 'Data Scientists' are cool!"
print(x)

#########################################################################

#Exercise 5 (Dictionaries)

Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
#1. print size values
shoe_size = Shoes["size"]
print(shoe_size)

#2.Nick to Adidas 
Shoes["brand"] = "Adidas"
print(Shoes)

#3. add key/value pair 
Shoes["type"] = "sneakers"
print(Shoes)

#4.  list of all the keys in the dictionary
keys_list = list(Shoes.keys())
print(keys_list)

#5.  list of all the values in the dictionary
values_list = list(Shoes.values())
print(values_list)

#6 check if key 'size exists
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")


#7. loop through
for key, value in Shoes.items():
    print(key, ":", value)
    
#8. remove color
del Shoes["color"]
print(Shoes)

#9. empty the dictionary
Shoes.clear()
print(Shoes)

#10. making a copy of the dictionary
_dict = {"key1": 1, "key2": 2, "key3": 3}
copy_of_dict = _dict.copy()
print(copy_of_dict)

#11. nested dictionary

# Define a nested dictionary
student = {
    "name": "Gasasira Joshua",
    "age": 30,
    "grades": {
        "OOP": 85,
        "DIM": 92,
        "REQ_ENG": 78
    },
    "contact": {
        "email": "gasasirajoshua@gmail.com",
        "phone": "0788225138"
    }
}

# Accessing dictionary values
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Math Grade:", student["grades"]["OOP"])
print("Contact Email:", student["contact"]["email"])
