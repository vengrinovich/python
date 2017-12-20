	
import datetime
import itertools


def menu():

	choice = (raw_input("""What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit: 
"""))

	# makes sure that when the function is done running, it
	# returns back to the menu unless user quits	
	if choice == '1':
		year_range()
		menu()
	elif choice == '2':
		month_year()
		menu()
	elif choice == '3':
		search_by_author()
		menu()
	elif choice == '4':
		search_by_title()
		menu()
	elif choice == 'Q' or choice == 'q':
		quit()
	else:
		print "Try again"
		menu()


def search_by_author():

	author = str(raw_input("Enter a title or a keyword from the author: "))

	with open('bestsellers.txt', 'r') as file_object:
		processed_file = file_object.read().split("\n")

	a = []
	b = []

	# separates each line into a separate sublist
	# and appends to variable a
	for sublist in processed_file:
		a.append(sublist.split("\t"))

	# returns all upper,lower and mixed case combination of author
	# so fox returns ['FOX', 'FOx', 'FoX', 'Fox', 'fOX', 'fOx', 'foX', 'fox']
	name_variations = map(''.join, itertools.product(*zip(author.upper(), author.lower())))

	for item in a:
		for name in name_variations:
			if name in item[1]:
				print item


def search_by_title():

	title = str(raw_input("Enter a title or a keyword from the title: "))

	with open('bestsellers.txt', 'r') as file_object:
		processed_file = file_object.read().split("\n")

	a = []

	# separates each line into a separate sublist
	# and appends to variable a
	for sublist in processed_file:
		a.append(sublist.split("\t"))
	
	# goes through each sublist and checks if the title (normal and capitalized)
	# keyword matches each title from the .txt file
	for item in a:
		if title in item[0] or title.capitalize() in item[0]:
			print item


def month_year():

	month = int(raw_input("Which month do you want to pick?: "))
	year = str(raw_input("Which year do you want to pick?: "))

	## opens the file and splits it at each new line, creating sublists of these lines
	with open('bestsellers.txt', 'r') as file_object:
		processed_file = file_object.read().split("\n")

	a = []

	# from each sublist/entry filters out the ones that match the year first
	# and appends them to variable a
	for sublist in processed_file:

		if year in sublist:
			a.append(sublist.split("\t"))

	# sorts through each item within the sublist
	for item in a:

		# third item in each sublist is date so this datetime module
		# to identify the example for extraction
		datee = datetime.datetime.strptime(item[3], "%m/%d/%Y")

		# datee.month extracts the month from each 3rd value on each iteration of the loop
		# and prints out the whole sublist if month matches the month entered
		if datee.month == month:
			print item


def year_range():

	year1 = str(raw_input("Which start year do you want to pick?: "))
	year2 = str(raw_input("Which end year do you want to pick?: "))

# opens the file and splits it at each new line, creating sublists of these lines	
	with open('bestsellers.txt', 'r') as file_object:
		processed_file = file_object.read().split("\n")

		# counts between every year between the the two dates
		# subsequent statements return lines with that year
		for year in range(int(year1),int(year2) + 1):

			a = []

			# for each sublist, checks if year is present and appends these lines to list a
			for sublist in processed_file:
				if str(year) in sublist:
					a.append(sublist.split("\t"))


			# for each item in sublists that were found, joins them together for better readability
			for item in a:
				print item

menu()


	




	

			


