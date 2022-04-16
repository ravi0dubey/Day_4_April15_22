
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total_names= len(names)
print(total_names)
random_number = random.randint(0,total_names-1)
print(random_number)
print(f"{names[random_number]} is going to buy the meal today")