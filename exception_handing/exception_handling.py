"""
exception handling
----------------------
- exception is an event and which will cause program termintaion

handling keys
--------------
try
except
else

"""
#-------------------Example----------------------------------------
# print("program starts")
# # print(x) # x is not defined anywhare 
# try:
#     print(x) # x is not defined anywhare 
# except:
#     print("exception occered")
# print("Program complete")


#-------------------Example----------------------------------------
# single except block
print("program starts")
print(10/5)
# print(10/0) #ZeroDivisionError: division by zero
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception occured......handled..")
print("Program complete")


#-------------------Example----------------------------------------
# multiple except block - try, except, else and finally
# any exception is then then except block will execue 
# if not execute any except block then execute else and finally block
# The finally block is always exicute
"""
except - execute only when exeption occured
else   - execute only exception mot occured
finally- always execute
"""
try:
    a = 10
    b = 5 #try with 0
    result = a/b
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Thrown ZeroDivisionError exception....")

except SyntaxError:
    print("Thrown SyntaxError exception....")

except:
    print("Exception handled....")
    
else:
    print("No Exceptions are occured")    
    
finally:
    print("Program ends...") 
    
 
#-------------------Example---------------------------------------- 
# Raising our own exeption

def enterage(number):
    if number < 0:
        raise ValueError("Only integers are allowed")
    if number % 2 ==0:
        print("Even number")
    else:
        print("Odd number")
        
number = -1 # try with negative numbers like -2, -1 any negative value
print("Checking the even/odd number y passing the function")
try:
    enterage(number)

except:
    print("Thrown ValueError exception...... and handeled....")

print("Program completed")









