"""
list
--------

- a list is collection which is ordered and changeble
- in python list are writtten with square brakets [].
- list is mutable
"""
# How to create a list
# =================================
#only integer in list
a = [1, 2, 3]
print(a)
#only String in list
b = ['apple', 'banana', 'cherry']
print(b)
#comination of string and integer in list
c = ["iphone", 49999, 'OnePlus']
print(c)
#empty list
d = []
print(d)


# how to accessing items from the list
# ==============================
a = ["Hello", "Python", "World"]
#to access 1st item
print(a[0])
# to get the last value
print(a[-1])


#multiple values based on index numbers
#===============================================
a = ['apple', 'banana', 'orange', 'cherry', 'kiwi', 'mango']
print(a[2:])
print(a[::-1])
print(a[-4:-1])


#Change item value
#===============================================
a = ['apple', 'banana', 'orange']
print(a)
#change apple with mango
a[0]='mango'
print(a)
# add kiwi as a first item
a.append()


#read the items by using loop statement
#===============================================
a = ['apple', 'banana', 'orange']

for item in a:
    print(item)


#check if the item is existing or not
#===============================================
a = ['apple', 'banana', 'orange']

if 'apple' in a:
    print("Yes, Apple is exist")
else:
    print("No, Apple is not exist")
    
    
#check total no of items
#===============================================
a = ['apple', 'banana', 'orange']

print(len(a))


#add new item to the list : append() or insert()
#===============================================
a = ['apple', 'banana', 'orange']

#append() it adds new item at the end of the existing list
a.append('Mango')
print(a)

#insert() it needs value along with index position 
a.insert(0,'kiwi')
print(a)


#remove item from the list : remove(), pop(), del, clear()
#===============================================
a = ['apple', 'banana', 'orange', 'mango', 'kiwi']

# pop() - here we are using only index numbers 
a.pop(0)
print(a)

# remove () - here we are using value of the item
a.remove('banana')
print(a)

# del - its is not function it is just keyword and here we have to use index number
del a[0]
print(a)

#clear() finction will clear all the list items
a.clear()
print(a)


#copy list
#===============================================
#approach 1
a = ['apple', 'banana', 'orange', 'mango', 'kiwi']
b = a

print(a)
print(b)

#approach 2 copy()
a = ['apple', 'banana', 'orange', 'mango', 'kiwi']
b=a.copy()
print(a)
print(b)


#join the multiple lists
#===============================================
#approach 1
a = ['apple', 'banana', 'orange']
b = ['mango', 'kiwi']
c = ['cherry']

d = a + b + c
print(d)

#approach 2 adding all the values in single list by using extend()
e = []
for item in a, b, c:
    e.extend(item)
print(e)

#approach 3 adding multiples list in one list as a sets by using append()
f = []
for item in a, b, c:
    f.append(item)
print(f)

