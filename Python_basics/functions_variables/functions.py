"""
function
-----------

function is a set of statements/block of code and which will perform a task
- function creation/declaration
- calling/invoking the function

1. function does not take aruguments then not return any value (None)
2. function does not take aruguments but returns some value
3. functions takes aruments but no return value
4. function takes arguments and also returns value

"""
# creating function and call the function
#--------------------------------
#create function
def myfun():
    print("Hello, \nThis is my first function")
# call the function
myfun()

# creating function with single parameter/argument
#--------------------------------
def myfun(name):
    print('Hello', name)
# call the function
myfun('Dileep')


# creating function with multiple parameters/arguments
#--------------------------------
def myfun(a,b,c):
    d = a + b + c
    print(d)
# call the function
myfun(12,4,4)

# return function with multiple parameters/arguments
#--------------------------------
def cal(a,b):
    return (a+b)

sum = cal(5,4)
print(sum)
#or
print(cal(5,4))

# return function with None value
#--------------------------------
def abc():
    return

print(abc())


# function can return multiple values
#--------------------------------
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
    
print(largest(100,50))
print(largest(10,50))






