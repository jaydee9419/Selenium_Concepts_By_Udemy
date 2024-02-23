"""
dictionary
----------------
- A dictionary is a collection which is unordered.
- mutable means we can do changes.
- it accepts index maping
- writting with curly brackets and they have key and key value
- key value can same data but key should be always uniqe

"""

# creating dictionary
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
print(a)

# access items form the dictionary key value
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
print(a['Apple'])
print(a['Oneplus'])
print(a['Samsung'])

# using get function
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
print(a.get('Apple'))

# how to change key values not keys from the dictionary
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
print(a)
a['Oneplus'] = 'OnePlus 10 Pro'
print(a)

#reading items from dictionary
#-----------------------------------------
# get item key only
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
for item in a:
    print(item)
    
# get item key value
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
for item in a:
    print(a[item])
    #or
for item in a.values():
    print(item)

# get item keys anf key values
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}

for x, y in a.items():
    print(x, ':' ,y)

# checking key is exist in dictionary or not
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
if 'Apple' in a:
    print('Yes')
else:
    print('No')
#or
print('Apple' in a) # return True/False

# find total number of items in dictionary
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
print(len(a))

# Adding items to the dictionary
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
a['Realme'] = 'Narzo' # we can't add multiple items in a single statement
print(a)

# Remove items to the dictionary
#-----------------------------------------
# pop() function to delete specific item
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
a.pop('Apple')
print(a)
# del keyword to delete specific item
del a['Samsung']
print(a)
# clear all the items from the dictionary
a.clear()
print(a)

# copy items form one dictionary to another
#-----------------------------------------
a = {'Apple': 'Iphone', 'Oneplus': 'Nord', 'Samsung': 'Galaxy'}
b = a
print(b)
# or
b=a.copy()
print(b)