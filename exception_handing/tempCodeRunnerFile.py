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
