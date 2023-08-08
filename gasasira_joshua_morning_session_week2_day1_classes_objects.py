class Circle:
    
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        print(pi*(self.radius**2))
        
    def circumference(self):
        pi=3.14
        print(2*pi*self.radius)

print('Circle exercise')
circle1=Circle(4)
print("the radius is",circle1.radius)
circle1.area()
circle1.circumference()
print('...................................................................')

class Employee:
    
    def __init__(self,paycheck):
        self.paycheck=paycheck
    def employee_bonus(self):
        return 0.15*self.paycheck
        
print('Employee exercise')
employee1=Employee(150000)
print('employee1 earns a paycheck of',employee1.paycheck, 'and a bonus of', employee1.employee_bonus())

employee2=Employee(230000)
print('employee2 earns a paycheck of',employee2.paycheck, 'and a bonus of', employee2.employee_bonus())
print('...................................................................')

#convert celcius to fahrenheit
class Temperature:
    def __init__(self,celsius):
        self.__celsius = celsius
    
    # convert to fahrenheit                  
    def fahr(self): 
        return (f"{temp1.__celsius} °C is {(9/5)*self.__celsius + 32} °F")

#creating object and calling methods on it
temp1 =Temperature(37)
temp1.__celsius=100
print(temp1.fahr())
print('...................................................................')

#ASSIGNMENT
#show encapsulation with employee information to give a pay incrementation(salary with employee info to new_salary e.g from 850k to 1m)

#class employee 
class Employees():

    def __init__ (self, name,age,role,salary):
        self.__name = name
        self.__age = age
        self.__role= role
        self.__salary = salary
        
    def display_info(self):
        print (f"{ self.__name} who is {self.__age} and the acting {self.__role} has a salary of {self.__salary} ")
        
    #method to change salary    
    def set_new_salary(self,new_salary):
        self.__salary=new_salary
        return self.__salary
#create new employee object 
emp1 =Employees("John",46,'operations manager',850000)
emp1.set_new_salary(1_000_000)
emp1.display_info()