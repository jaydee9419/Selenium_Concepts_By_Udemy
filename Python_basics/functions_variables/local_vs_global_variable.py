"""
variables
-------------
variable is a container and which contains some data

Global vs Loval variable
---------------------------
Global: a variable create outside of the function are called as Global variable
Local: a variable create inside of the function are called as Local variable

"""
#example 1
#----------------------------------
a = 20 # 'a' is global variable

def cal():
    b = 10 # 'b' is local variable
    sum = a + b
    print(sum)
cal()

#example 2
#----------------------------------
a = 20 # 'a' is global variable
def cal():
    a = 10 # 'a' is local variable
    print(a)
cal()

#example 3 changing local variable to global variavle
#----------------------------------
a = 20 # 'a' is global variable
def cal():
    global a
    a = 10 # 'a' is global variable
    print(a)
cal()
print(a) # getting 10 because we have change variable value and local change to global

#example 4 changing local variable to global variavle
#----------------------------------
def cal():
    global a
    a = 10 # 'a' is global variable
    print(a)
cal()
print(a)  # 'a = 10' is global variable
a = 20 # 'a' is global variable
print(a) # getting 20 because we have change global variable value 





