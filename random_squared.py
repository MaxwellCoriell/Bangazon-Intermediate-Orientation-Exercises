# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.

import random #needed to run random

print(random.randint(0,49)) #generate a random number from 0-49
print("------------------")

random_numbers = random.sample(range(0,49), 20)
print(random_numbers)
print("------------------")

# With the resulting list, use a list comprehension to build a new list that contains each number squared. 
# For example, if the original list is [2, 5], the final list will be [4, 25].

for number in random_numbers:
	squared_numbers = [number * number]
	print(squared_numbers)