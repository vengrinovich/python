#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.

def common_numbers(list1, list2):
	a = []

	for number in list1:
		if number in list2:
			a.append(number)
	print a
	print len(a)


with open('primenumbers.txt') as primenumbers_object:
	primenumbers = primenumbers_object.read()
	x = primenumbers.split()
	
with open('happynumbers.txt') as happynumbers_object:
	happynumbers = happynumbers_object.read()
	y = happynumbers.split()

	common_numbers(x,y)

