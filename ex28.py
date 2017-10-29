#Implement a function that takes as input three variables, and returns the largest of the three. 
#Do this without using the Python max() function!
import random

numbers = [random.sample(range(0,5),3)]
a = []


if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
	a.append(numbers[0])
elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
	a.append(numbers[1])
elif numbers[2] > numbers[0] and numbers[2] > numbers[1]:
	a.append(numbers[2])

print numbers
print a
