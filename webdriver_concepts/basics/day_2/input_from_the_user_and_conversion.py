# always consider as string type what ever the input given by using input except int(input()) 
#----------------approach - 1--------------
num1 = input("Please enter 1st number: ")
num2 = input("Please enter 2nd number: ")

print(type(num1))
print(type(num2))

print(num1, num2)
#----------------approach - 2--------------
#getting input via int method
num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

print(type(num1))
print(type(num2))

print(num1, num2)

#----------------approach - 3--------------
#conversion string to int
num1 = input("Please enter 1st number: ")
num2 = input("Please enter 2nd number: ")

print(type(num1))
print(type(num2))

print(int(num1) + int(num2))

#----------------approach - 4--------------
#conversion string to float
num1 = input("Please enter 1st decimal number: ")
num2 = input("Please enter 2nd decimal number: ")

print(type(num1))
print(type(num2))

print(float(num1) + float(num2))







