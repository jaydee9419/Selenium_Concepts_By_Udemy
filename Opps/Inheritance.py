"""
inheritance - reusability
------------------
- aquiring all the attributes(variables) and behaviour(methods) from one class t another class is called as inheritance
class A: 
    variables: a,b,c
    methods: m1(), m2()

class B(A): 
    variables: a,b,c
    methods: m1(), m2()
    
concluion:   
- A is parent/Base/super class of B class
- B is child/sub/derived class of of A class

benefits
-----------
- code re-usability
- avoid duplication

types
----------
1. single       ----> one parent and one child
2. multi level  ----> parent ---> child1 ---> child2 ---> child3 ---> child4 (child4 can access all preceeding classes)
3. heirarchy    ----> one parent and multiple child
4. multiple     ----> multiple parent and one child
"""

# 1. single  ----> one parent and one child
# --------------------------------------------
# Eg - 1
from multiprocessing import Manager
from re import X


class A:
    def method1(self):
        print("This is method1 from class A")

class B(A):
    def method2(self):
        print("This is method2 from class B")

obj = B()
obj.method1()
obj.method2()

# Eg - 2
class A:
    x = 10
    y = 20
    def method1(self):
        print("This is method1 from class A")
    
    def multi(self):
        print(self.x*self.y) # acessing same class variables

class B(A):
    a = 5
    b = 10
    def method2(self):
        print("This is method2 from class B")
        
    def sub(self):
        print(self.a-self.b) # acessing same class variables
    
    def sum(self):
        print(self.x+self.y) # acessing parent class variables in child class

obj = B()
obj.method1()
obj.multi()
obj.method2()
obj.sub()
obj.sum()


# 2. multi level  ----> parent ---> child1 ---> child2 ---> child3 ---> child4 (child4 can access all preceeding classes)
# --------------------------------------------------------------
class A:
    x = 10
    y = 20
    def method1(self):
        print("This is method1 from class A")

class B(A):
    a = 5
    b = 10
    def method2(self):
        print("This is method2 from class B")

class C(B):
    m = 5
    n = 10
    def method3(self):
        print("This is method3 from class C")
        
    def div(self):
        print(self.n/self.m) # accessing same class variables in same class
        
    def multi(self):
        print(self.x*self.y) # acessing A class variables through B in C class
        

    def sub(self):
        print(self.a-self.b) # acessing B class variables in C class

obj = C()
obj.method1()
obj.method2()
obj.method3()
obj.multi()
obj.div()
obj.sub()


# 3. Heirarchy  ----> one parent and multiple child
# --------------------------------------------
class Father:
    name = 'Harsha'
    job = 'Manager'

    def details(self):
        print(f"Hello, this is {self.name}.")
        print(f"I am working as {self.job}")
        print('------------------------------------------')

class Dileep(Father):
    name = "Dileep"
    job = "Developer"

    def details(self):
        print(f"Hello, this is {self.name}.")
        print(f"my father is {Father.name}.")
        print(f"I am working as {self.job}")
        print('------------------------------------------')

class Rakesh(Father):
    name = "Rakesh"
    job = "Automation Tester"

    def details(self):
        print(f"Hello, this is {self.name}.")
        print(f"my father is {Father.name}.")
        print(f"I am working as {self.job}")
        

father = Father()
father.details()

son1 = Dileep()
son1.details()

son2 = Rakesh()
son2.details()


# 4. multiple  ----> Multiple parants and one child
# --------------------------------------------
class Father:
    name = 'Janardhan'
    job = 'Manager'

    def details(self):
        print(f"Hello, this is {self.name}.")

class Mother:
    name = "Archana"
    job = "Assist Manager"

    def details(self):
        print(f"Hello, this is {self.name}.")
        print(f"I am working as {self.job}")

class Rakesh(Father, Mother):
    name = "Dileep"
    job = "Automation Tester"

    def details(self):
        print(f"Hello, this is {self.name}.")
        print(f"my father is {Father.name}.")
        print(f"my mother is {Mother.name}.")
        print(f"I am working as {self.job}")
        

father = Father()
father.details()

son1 = Mother()
son1.details()

son2 = Rakesh()
son2.details()


# how to invoke same name methods or variables both the classes and how to use in required class 
# --------------------------------------------
class A:
    def display(self):
        print("This is method from class A")

class B(A):
    def display(self):
        print("This is method from class B")

obj = B()
obj.display() # overriding: here i can see only display method from class B

# how to overcomee the overriding probelm 
# by using super key word
class A:
    name = "jay"
    def display(self):
        print("This is method from class A")

class B(A):
    name = "dee"
    def display(self):
        print("This is method from class B")
        super().display() # this super keyword will go to class A and invike the display method in clawss B
        print(f"{super().name} {self.name}")
obj = B()
obj.display() 

