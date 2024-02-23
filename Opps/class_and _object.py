"""
class and object
---------------------
class 
- collection of variables(attributes) & methods(behaviour)
- is bluprint of object(logical entity)
- does not occupy any space in the entity

object
- object is an instance of class
- physical entity
- occupy certain space in the memory

for one class, we can create multiple objects
but objects are independent

function vs method
- if we create same function with in the function is callsed Method
- if we create function without class is named as function/general function
"""

"""
type of methods we can define wit in the class
1. instance method (we can call only through object)
2. static method (we can directly cal using class)
"""
#how to create class with instance method
#-----------------------------
from cgi import print_environ
from curses.ascii import EM


class Myclass:
    def myfun(self):
        pass
    def display(self, name):
        print(name)
        
obj=Myclass()

obj.display("Dileep")
obj.display("Rakesh")


#how to create class with static method
#-----------------------------
# annotation: @staticmethod
class Myclass:
    def myfun(self): # here the self is reffering to the class
        print('This is instance method')
        
    @staticmethod
    def display(self, name): # here self is condider as a perameter
        print(self, name)
        
obj=Myclass()
obj.myfun()
obj.display('Dileep', 'Muvvala')
#or
Myclass.display('Divya', "ravuri")
# Myclass.myfun() # This will generate en error because this method only applicable only for staticmethod not instance method


#combination of global vaiable, class variable and local variable
#-----------------------------
a = 20 # global variable
class Myclass:
    b = 10 # class variables
    def sum(self):
        c = 15 # Local variable
        # print(a + b + c) # we can not access class variables directly inside methods
        print(a + Myclass.b + c)
    def mul(self):
        c = 10
        print(a*Myclass.b*c)

obj = Myclass()
obj.sum()
obj.mul()

#or

a = 20 # global variable
class Myclass:
    b = 10 # class variables
    def sum(self):
        c = 15 # Local variable
        # print(a + b + c) # we can not access class variables directly inside methods
        print(a + self.b + c)
    
    def mul(self):
        c = 10
        print(a*self.b*c)

obj = Myclass()
obj.sum()
obj.mul()


#using same global vaiable, class variable and local variable
#-----------------------------
a = 5 # global variable
b = 10 # global variable
class Myclass:
    a = 15 # class variables
    b = 20 # class variables
    def sum(self, a, b):
        print(a, b) # local variables
        print(self.a, self.b) # class variable
        # accessing global variables
        print(globals()['a'], globals()['b']) #global variables

obj = Myclass()
obj.sum(25, 30)


#multiple objects for a single class
#-----------------------------
class Myclass:
    def display(self, name):
        print(f"This is {name}")
        

obj = Myclass()
obj.display('Dileep')

obj2 = Myclass()
obj.display("Satya")

obj3 = Myclass()
obj.display('Harsha')

"""
method
--------
- give any name
- return the values
- method can take arguments/perameters
- we have to use an object invoke the method


constructor
------------
- name is fixxed: def __init__(self):
- constructor will not return any value
- constructor can also take arguments/parameters
- constructor will be called at the time of object creation

"""

#constructor (without calling method we can get he data from the method)
#-----------------------------
class Myclass:
    name = "Jay Dee"
    def __init__(self, name):
        print(f"am {self.name}")
        print(f"My friend is {name}")
        

obj = Myclass('Dileep')
obj2 = Myclass('Harsha')
obj3 = Myclass('Satya')

# how to crete class variable inside constructor
#-----------------------------
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        #below steps are converting the below __init__ method local variable in to class variable
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employeee name: {self.emp_name}")
        print(f"Employee salary: {self.emp_salary}")

obj = Employee(111, 'Jaydee', 10000)
obj.display()
obj2 = Employee(112, 'Dileep', 20000)
obj2.display()
obj3 = Employee(113, 'Rakesh', 30000)
obj3.display() 

# how to print data without method this is applicableonly for string type data
#-----------------------------
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        #below steps are converting the below __init__ method local variable in to class variable
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        
    def __str__(self):
        return self.emp_name
obj = Employee(111, 'Jaydee', 10000)
print(obj) # this will return only string value







