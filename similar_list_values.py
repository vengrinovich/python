"""Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes."""

"""two ways are shown, with and without list coprehension"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = [i for i in a if i in b]

for number in a:
	if number in b:
		c.append(number)

print list(set(c))
print list(set(d))
