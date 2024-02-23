"""
we have open() pre defined method and in that we have to pass 2 values
1. file path
2. file mode (read/write/append)
    w - writting
    r - read
    a - appendin
    
note: if file is not there then create new file with given path and name
"""
# How to add some data into a exiting text file
#-------------------------------------------------
path = 'C:\\Users\\11571\\Downloads\\sample.txt'
file = open(path, 'w')
file.write("Hello,\nGood Morning!!..\n\nThis is just sample data\n")
file.close()
print("Program completed")

# How to read data from exiting text file
#-------------------------------------------------
path = 'C:\\Users\\11571\\Downloads\\sample.txt'
file = open(path, 'r')
data = file.read()
print(data)
file.close()

# How to append data to exiting text file
#-------------------------------------------------
path = 'C:\\Users\\11571\\Downloads\\sample.txt'
file = open(path, 'a')
file.write("\nThank You")
file.close()
print("Program is completed")







