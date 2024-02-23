
def count():
    for number in range(1, 11):
        print(number)

count()


a = 123

b = str(a)

print(a)
print(type(a))
print(b)
print(type(b))



# String
my_word = "Hallo"

# Count occurrences of 'a'
count_a = my_word.count('a')

# Print the result
print("Number of 'a' letters:", count_a)


movie_name = input("Please enter movie name: ")
duration = float(input("Please enter Duration: "))
episodes = float(input("Please enter the no of episodes: "))


if duration >=1:
    
    if episodes >= 10:
        print(f"{movie_name} is a webserise")
    else:
        print(f"{movie_name} is a Movie")
elif duration <=1:
    if episodes >= 10:
        print(f"{movie_name} is a serial")
    else:
        print(f"{movie_name} is a shortfilm")
    

