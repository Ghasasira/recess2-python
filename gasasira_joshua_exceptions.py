"""
this is an example of
multiline commenting 
in python
"""
# This is a single line comment

# Variables of different types

# string
# name = "Alice"
# print("Name:", name, "Type is:", type(name))
 
# # integer
# age = 25
# print("Age:", age, "Type is:", type(age))

# # float 
# height = 1.65 
# print("Height:", height, "Type is:", type(height))

# # boolean
# is_student = True 
# print("Is student:", is_student, "Type is:", type(is_student))

# # list
# hobbies = ["reading", "coding", "music"] 
# print("Hobbies:", hobbies, "Type is:", type(hobbies))

# # dictionary
# grades = {"java": 90, "c#": 85, "python": 95} 
# print("Grades:", grades, "Type is:", type(grades))

# #for loop
# fruits =['mango','orange','apple',]

# for fruit in fruits:
#     print(fruit)

#summary
numbers=[]
while len(numbers)<5:
    try:
        x=int(input('enter a number:'))
        if x%2==0:
            print (f'{x} is a even number')
            numbers.append(x)
        else:
            print (f'{x} is an odd number')
            continue


    except Exception as exc:
        print(f'{exc.__class__.__name__} has occured ')
        print('please enter a valid number')
    finally:
        print('continue')
else:
    print ('all the elements are added to the list')
    for number in numbers:
        print(number)
            
        
    