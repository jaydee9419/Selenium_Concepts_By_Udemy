#input
#----------approch - 1------------
name = "Jay"
age = 30
salary = 49999.99

#----------approch - 2------------
# name, age, salary = "jay", 30, 49999.99


#output
#----------approch - 1------------
print(name)
print(age)
print(salary)
print("============================")

#----------approch - 2------------
print(name, age, salary)
print("============================")

#----------approch - 3------------
print("Name is ", name)
print("Age is ", age)
print("Salary is ", salary)
print("============================")

#----------approch - 4------------
print(f"Name: {name}\nAge: {age}\nSalry: {salary}")
print("============================")

#----------approch - 5------------
#note: %s is string, %d is digit and %g decimal number digit like floting number
print("Name: %s \nAge: %d\nSalry: %g" %(name, age, salary))
print("============================")

#----------approch - 6------------
#note: %s is string, %d is digit and %g decimal number digit like floting number
print("Name: {} \nAge: {}\nSalry: {}" .format(name, age, salary))
print("============================")


