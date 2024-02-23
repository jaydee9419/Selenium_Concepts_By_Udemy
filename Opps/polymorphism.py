
"""
Polymorphism
--------------
- means many forms
- Eg: shape will be circle, rectangle, square
- polymorphism we can implement by using overloading concept
"""

# 1. Overriding method
#-----------------------------------

class Bank:
    def rateofinterest(self):
        return 0

class Sbi_bank(Bank):
    def rateofinterest(self):
        return 15

class Axis_bank(Bank):
    def rateofinterest(self):
        return 18

obj1 = Sbi_bank()
print(obj1.rateofinterest())

obj2 = Axis_bank()
print(obj2.rateofinterest())


# 2. Overloading method
#-----------------------------------
#Eg - 1
class Human:
    def sayhello(self, name=None):
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello")   
            
obj = Human()
obj.sayhello()
obj.sayhello("Dileep")


#Eg - 1
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

obj = Calculation()
obj.add()
obj.add(1)
obj.add(1,2)
obj.add(1,2,3)







