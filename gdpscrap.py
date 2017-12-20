

def average_unemployment(filename, year):

	a = ''

	# csv file opens with each row separately in terminal
	# each row becomes a string when using split
	with open(filename, 'r') as file_object:
		processed_file = file_object.read().split()



	#appends the row of numbers to a, that match the year specified
	for i in processed_file:
		if year in i:
			a += i

	# puts comma separated values from the row into a list where they are all separate values as opposed to
	# one big string		
	a = a.split(',')
	
	# eliminates the year and the space in the end from variable a
	values = (a[1:len(a)-1])

	# converts values into floats so that math is possible on them
	values = [float(x) for x in values]

	average = sum(values) / len(values)

	print values, average


average_unemployment('unemp.csv', '1992')