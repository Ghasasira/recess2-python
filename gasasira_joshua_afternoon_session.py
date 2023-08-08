#EXERCISE

# 1. dictionary exercise
#enter new key-value pair
my_dict = {'key1': 'value1'}

my_dict['key2'] = 'value2'

print(my_dict)

#change
my_dict['key1'] = 'new value'
print(my_dict)

#update
my_dict.update({'key3': 'value3', 'key1': 'updated value'})

print(my_dict)

#check if it exists
if 'key2' in my_dict:
    print("The key 'key2' exists in the dictionary.")
else:
    print("The key 'key2' does not exist in the dictionary.")
    
#loop dictionary items 

for key, value in my_dict.items():
    print(key, value)

#delete\remove item
del my_dict['key3']
print(my_dict)

# 2. string exercise
#Using len()
my_string = "Hello, World!"
length = len(my_string)
print(length)

#loop through string
for x in my_string:
    print(x)
    
#slicing in strings
substring = my_string[7:12]
print(substring)

substring2 = my_string[::2]
print(substring)

# 3. Use a condition to show how to use booleans
age = int(input('enter your age:'))
question=input('are you a student (enter y for yes or n for no):').lower()
if(question=='y'):
    is_student = True
if(question=='y'):
    is_student = False
    
else:
    print('enter valid response')
    exit()
    
# Check if the person is a student and their age is less than 30
if is_student and age < 30:
    print("The person is a student and their age is less than 30")
else:
    print("The person is either not a student or their age is not less than 30")


#lesson summary
#dict
#any data type
#ordered but do not allow duplicates
mydict = {
    "phone" : "iphone",
    "iphonemodel": "iphone15"
}
print (mydict)

#length of a dictionary
print(len(mydict))
#data type
print(type(mydict))
#access dictionary items
print(mydict["phone"])
print(mydict.get("iphonemodel"))

print(mydict.keys())


#Exercise one: use the values() method to return a list of all values in the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
values_list = list(my_dict.values())
print(values_list)


#Exercise two: to check if a key does exist in your dictionary
#exercise three: give an example on how to change dictionary items, how to update
#exercise four: give an exampole on how to add dict items, how to remove dict items
#exercise five: give an example on how you can loop through a dictionary and also how to nest dictionaries



#Numbers
#type conversions
w = 10
r = 5.9
z = 2j

z = complex (w)
print (w)
print(type(z))

#convert from int to float
r = float (w)
print (w)
print(type(r))

#convert from float to complex
z = complex (r)
print (r)
print(type(z))

#convert from complex to float
r = float (z)
print (z)
print(type(r))


#CASTING
#specify a variable type
h = int(20) #h is 20

#strings
print("afternoon")
print('after')

#strings as arrays
a = "afternoon"
print(a[0])


#Exercise one: Use the len() function to determine the length of the string
#Exercise two: give an example of a for loop in a string
#Exercise three: give an example of slicing in strings



#how to modify strings
a = "afternoon"
print(a.lower())
print(a.upper())

#remove whitespace
b = "  after  noon "
print(b.strip())

#string concatenation
c = "Afternoon"
d = "class"
w = c+d
print('c' + '' + 'd')
print(w)


#format strings
#works when one is trying to combine a strng to a number
#the format() takes the passed parameteers formats them and palces them in the string where the placeholders {} are

age = 23
name = "My name is Arnold and I am {}"
print(name.format(age))

#boolean
#these evaluate to a true or false
print(bool(15))

