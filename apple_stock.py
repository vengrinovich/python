import csv
import itertools
import datetime
import pandas as pd 

def get_input_descriptor():

	with open ('table.csv', 'rb') as file_object:

		# skips first title line of the csv file
		# groups the rows together into one big list
		skip_first_line = file_object.readlines()[1:]
		
		# reader function generates a reader object
		# The reader function is designed to take each line of the file and make a list of each row separately. 
		# Then, you just choose the row value(s) you want the information for.
		reader = csv.reader(skip_first_line)

		get_data_list(reader)

def get_data_list(table_file_processed):		

		# creates an empty list of tuples
		my_tuple = list(())
		
		# takes specific row values from each row in the .csv file
		# and adds them to my_tuple in pairs, like ('1984-09-11', 3.02), etc.
		for row in table_file_processed:
			my_tuple += ((row[0],float(row[6])),)

		average_date(my_tuple)

def average_date(tuples_list):
	
	# takes value from previous function and creates a data frame with
	# column names year & value and rows like: 0  2013-02-08  474.98 
	df = pd.DataFrame(data = tuples_list, columns=['year','value'])

	# makes sure that the date column is in the right datetime format
	# so later you can easily extract date, month or year from it
	df['year'] = pd.to_datetime(df['year'])

	# groups the values month-year in the first column, uses strftime values for month and year
	# then sums the values of grouped items, sorts them and returns
	dff = df.groupby(df['year'].dt.strftime('%m-%Y'))['value'].mean().sort_values()

	print dff


	# this below is the same as above but using a simple example;
	"""x = [('2002-05-01', 968), ('2002-04-01', 155), ('2002-04-01', 155), ('2003-07-01', 578), ('2003-01-01', 973)]

	# creates an dataframe where each values in sublist a is a sepate row with column names year & column,
	df = pd.DataFrame(data = x, columns=['year','number'])

	# makes sure that the date column is in the right datetime format
	# so letter you can easily extract date, month or year from it
	df['year'] = pd.to_datetime(df['year'])
	
	# groups the values month-year in the first column, uses strftime values for month and year
	# then sums the values of grouped items, sorts them and returns
	dff = df.groupby(df['year'].dt.strftime('%m-%Y'))['number'].sum().sort_values()

	print dff"""


get_input_descriptor()

