# always use the csv module for reading and writing CSV files
# this is the CSV file used in this example program:

"""4/5/2015 13:34,Apples,73
4/5/2015 3:41,Cherries,85
4/6/2015 12:46,Pears,14
4/8/2015 8:59,Oranges,52
4/10/2015 2:07,Apples,152
4/10/2015 18:10,Bananas,23
4/10/2015 2:40,Strawberries,98"""

import csv 

def example1():

	with open ('example.csv') as file_object:

		# returns a reader object for you to use
		# a reader object lets you iterate over lines in the CSV file
		# to read data from a CSV file you need to create a reader object
		# if you were to print the below, it returns <_csv.reader object at 0x10e168360>
		reader_object = csv.reader(file_object)

		# puts each row in a separate sublist and comma separates values in each sublist
		# example: [['4/5/2014 13:34', 'Apples', '73'], ['4/5/2014 3:41', 'Cherries', '85']
		exampleData = list(reader_object)
		
		# returns 4/5/2015 13:34
		print exampleData[0][0]
		# returns Apples
		print exampleData[0][1]
		# returns Bananas
		print exampleData[5][1]

def example2():

	with open ('example.csv') as file_object:

		reader_object = csv.reader(file_object)	

		# loops through the rows in the reader object, each row is a list
		# of values like ['4/5/2014 13:34', 'Apples', '73']
		for row in reader_object:

			# print a string 'Row #', then uses reader object's line_num variable
			# which contains the number of the current line, adds a spacebar, and finally
			# the list of values, i.e. Row #1 ['4/5/2014 13:34', 'Apples', '73']
			print('Row #' + str(reader_object.line_num) + ' ' + str(row))


def example3():

	# this example creates a CSV file and adds two rows with custom values to it
	# open the file in write mode. If newline argument does not pass a blank string,
	# on windows the rows will be double-spaced
	with open ('output.csv', 'w') as file_object:

		# a writer object lets you write data to a CSV file, use csv.writer() to create a writer object
		writer_object = csv.writer(file_object)

		
		# The writerow() method for Writer objects takes a list argument. 
		# Each value in the list is placed in its own cell in the output CSV file.
		writer_object.writerow(['what', 'am', 'I', 'doing'])
		writer_object.writerow(['hello', '23', '+', '23'])

	file_object.close()


def example4():

	# separate cells with a tab character instead of a comma and makes the rows double-spaced
	# The delimiter is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. 
	# The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline.
	with open ('output.tsv', 'w') as file_object:

		writer_object = csv.writer(file_object, delimiter = '\t', lineterminator = '\n\n')

		writer_object.writerow(['what', 'am', 'I', 'doing'])
		writer_object.writerow(['hello', '23', '+', '23'])

	file_object.close()


example1()
example2()
example3()
example4()

