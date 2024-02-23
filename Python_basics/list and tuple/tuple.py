"""
tuple
-------------------------
- a tuple is a collaction which is ordered and unchangeable.
- in python tuple are written with round brackets
- tuple is immutable
- tuples are more secure then the list

"""
# how to creating tuple
# ======================================
# a = ('Apple', 'Banana', 'Mango', 'Kiwi', 'Orange')
# b = (1, 2, 3, 4, 5)
# c = ('Iphone', 49999, 'OnePlus')
# d = ()

# print(a)
# print(b)
# print(c)
# print(d)


# access indidual item from the tuple 
# ======================================
# based on index
# a = ('Apple', 'Banana', 'Mango', 'Kiwi', 'Orange')

# print(a[1])
# print(a[-1])
# print(a[2:4])
# print(a[::-1])

# change the tuple items - not possible
# ======================================
# based on index
a = ('Apple', 'Banana', 'Mango', 'Kiwi', 'Orange')
print(a)
"""
# we cannot modify exiting value
# we cannot append exiting value
# we cannot insert exiting value
# we cannot remove exiting value
"""
# By default tuple does not allow you to change values because it it immutable 
# There are few operations we can do 
# we can convert tuple in to a list and do changes what ever we want and change back to touple again

# tuple ---> list(modify) ---> tuple

b = list(a)
print(b)

b[0] = "Dragan"
print(b)
c = tuple(b)
print(c)















