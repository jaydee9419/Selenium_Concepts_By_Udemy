"""
set
----------------
- set is a collection which is unordered and unindexed.
- in python sets are written with curly brakets.
- set is mutable and we can perform all the actions
"""
# creating sets
#--------------------------------
from ctypes import Union


a = {1, 2, 3, 4}
b = {'Apple', 'Mango', 'Kiwi', 'Orange'}
c = {'Iphone', 49999, 'OnePlus'}

print(a)
print(b)
print(c)

# accessing items from set
#--------------------------------
a = {'Apple', 'Mango', 'Kiwi', 'Orange'}
#only one approach is by using loop and we can not extract specific item from set
for item in a:
    print(item)
print("Done!!!...")\
    

# to check value is exit in the set
#--------------------------------
a = {'Apple', 'Mango', 'Kiwi', 'Orange'}
for item in a:
    if 'Apple' in item:
        print("Yes, apple is there.")
    #or
print('Kiwi' in a)


# adding items to the set by using add() / update()
#--------------------------------
# add() is using to add single item at a time
a = {'Apple', 'Mango', 'Kiwi', 'Orange'}
a.add('Banana')
print(a)
# update() is using to add multiple items at a time
a = {'Apple', 'Mango', 'Kiwi', 'Orange'}
a.update(['Watermeloon', 'Guvva'])
print(a)


# remove items
# -remove() 
# -discard()
# in remove function if non existing item remove() it through error and in discard() not shown any error and rest working both are same
#--------------------------------
a = {'Apple', 'Mango', 'Kiwi', 'Orange'}
# remove item (index will ot work so we have to use item value directly)
# remove()
a.remove('Apple')
print(a)
# discard()
a.discard('Orange')
print(a)
# pop() always index method using and it won't applicable
# a.pop('Mango') pop always choose index value
# print(a)
# clear() remove all the items
a.clear() #(remove all the items from the set)
print(a)

# delete complete set variable 'a'
del a
print(a) # NameError: name 'a' is not defined (because 'a' already deleted)


# joining multiple sets
#--------------------------------
 # +: cancatination not work
 # union() is applicable fpr the sets
a = {'Apple', 'Mango'}
b = {'Kiwi', 'Orange'}
c = {"Guvva"}

d = a.union(b,c)
print(d)

# or
# passing all sets to emply set with out changing original variable
e = set()
f = e.union(a,b,c)
print(f)


# update set
#--------------------------------
a = {'Apple', 'Mango'}
b = {'Kiwi', 'Orange'}
c = {"Guvva"}
a.update(b,c)
print(a)
 