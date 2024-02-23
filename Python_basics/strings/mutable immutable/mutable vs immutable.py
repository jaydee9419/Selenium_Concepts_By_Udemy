"""
Mutable -  Can not change the value of the variable
imMutable - Can change the value of the variable

- strings   :  Strings in Python are immutable, meaning you cannot change the characters of a string once it's created. If you need to modify a string, you create a new one.
- tuple     : Tuples are similar to lists, but they are immutable. Once a tuple is created, you cannot modify its contents.
- list      : Lists in Python are mutable, meaning you can modify their contents by adding or removing elements, or by changing the values of existing elements.
- dictionary: Dictionaries are mutable, allowing you to add, modify, or remove key-value pa
"""

#====================================
#how the memory will change
# id is nothing but memory for a variable
a = "Hello"
print(id(a))

# if the value is change then it is immutable
a = a + "World"
print(id(a))

#==================================
# how to use + and * with the string in variable
# +: will do concatination
# *: will do multipluication 

a = "Hello"
print(a + " World") # +: will do concatination
print(a * 2) # *: The star will print two times of variable