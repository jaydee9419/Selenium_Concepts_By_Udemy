"""
break
"""
# # by passing one if condition we can exit the forloop (if range goes to 5 number its calls break function)
# for number in range(1,11):
#     if number == 5:
#         break
#     print(number)
    
# print("Program exited!!!...")


"""
continue
"""

# if we pass continue command and the requirement fullfilled
#then below continue statements will not exicute and it will goo back to the main 
# in the below example one reached 5 then print not exucuted and this will jump to next item
# by passing one if condition we can exit the forloop (if range goes to 5  and 7 and 9 numbers its calls break function)
for number in range(1,11):
    if number == 5 or number == 7 or number == 9:
        continue
    print(number)
    
print("Program exited!!!...")