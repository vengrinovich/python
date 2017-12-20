
def main():

	gdp_file = raw_input("Please provide GDP data filename: ")
	unemp_file = raw_input("Please provide unemployment data filename: ")
	year = raw_input("What year would you like to check (1948 - 2008): ")

	gdp = average_gdp(gdp_file, year)
	unemployment = average_unemployment(unemp_file, year)

	print "In %s the average GDP was %s and the average unemployment was %s" % (year, gdp, unemployment)

def average_gdp(gdp_file, year):

	gdp_values = []
	a = []

	with open (gdp_file, 'r') as file_object:
		processed_file = file_object.read().split()
		#processed_file = processed_file

	# combines year/quarter with gdp value into joint strings, 'like 1947q2 -0,6'
	# appends result to variable a
	for x in range(0,len(processed_file),2): #the 2 in the end separates values into groups of two so it doesn't count the same ones
		a.append(processed_file[x] + processed_file[x+1])
	
	# checks if the year is present in every value in a (now joint with gpd)
	# and appends the gdp value to the gdp_values string
	for x in a:
		if year in x:
			gdp_values.append(x[6:])

	# converts values into floats so that math is possible on them
	gdp_values = [float(x) for x in gdp_values]

	averagegdp = sum(gdp_values) / len(gdp_values)

	return averagegdp

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

	averageunmp = sum(values) / len(values)

	return averageunmp
	
main()


