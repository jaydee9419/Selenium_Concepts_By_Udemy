"""
arguments/parameters
-----------------------
two types of parameters
1. positional 
2. keyword
"""

# positional arguments 
#--------------------------------
def details(name, age, gender):
    print(f"My name is {name}")
    print(f"am {age} old")
    print(f"sex: {gender}")

details("Dileep", 27, 'Male')


# keyword arguments 
#--------------------------------
def car(brand, price, model):
    print(f"Brand: {brand}")
    print(f"price: {price}")
    print(f"model: {model}")

car(model=2023, brand="Tata", price=500000)

# defult values assigned to keyword argumnts
#--------------------------------
# keyword aruguments will consider instade of default value
def car(brand="Bata", price=300000, model=2022):
    print(f"Brand: {brand}")
    print(f"price: {price}")
    print(f"model: {model}")

car(model=2023, brand="Tata", price=500000)

# defult values assigned to positional argumnts
#--------------------------------
# positional aruguments will consider instade of default value
def car(brand="Bata", price=300000, model=2022):
    print(f"Brand: {brand}")
    print(f"price: {price}")
    print(f"model: {model}")

car("Tata", 500000, 2025)

# combination of positional and keyword agruments
#--------------------------------
def car(brand, price, model):
    print(f"Brand: {brand}")
    print(f"price: {price}")
    print(f"model: {model}")

car("Tata", 500000, 2025)
car("Bata", 12000, model=2023)
# car(brand="Tayota", 5000, 2024) # wrong calling (positional argument must be appear before any keyword agrument) 





