import json
import calendar
from collections import Counter #A Counter takes a list and counts how many of each element were in the list. To use the Counter, first import it from collections:
from bokeh.plotting import figure, show, output_file

# gets the json data from dict and loads into variable birthday, then passes this on to function birthday_date
def dictionary():

	birthday = {}
	with open('dict.json', 'r') as openfile_object:
		birthday = json.load(openfile_object)
		months(birthday)

# get dictionary value from dictionary function and returns unique months and values
def months(birthday):

	dates = birthday.values() #extracts the dates from dictionary
	months = []
	months_names = []
	
	for i in dates:
		months.append(i[0:2])

	months_int = [int(i) for i in months] # takes values from months and turns them into integers

	for i in months_int:
		months_names.append(calendar.month_name[i]) #use calendar function to turn number of months into month name and append to a list after

	unique_values = Counter(months_names) #shows usnique value & count
	graph(unique_values)

# takes aggregated values of Month:Value from months function and draws a vertical bar graph
def graph(birthday_values):
	categories = ['May','January','February','October', 'September']
	output_file = ('birthday.html')

	keys = [x for x in birthday_values.keys()]
	values = [x for x in birthday_values.values()]

	plot = figure(x_range = categories) #range/amount of x values in the bottom
	plot.vbar(x= keys,top = values, width = 0.5, color = 'firebrick')

	show(plot)



dictionary()		

#takes files from dict.json and allows the user to ask for values
# asks for values to add to the list and updates the json. file with new values so that when
#the function is ran again, the initial dictionary will keep increasing
def birthday_date(birthdays):
	
	with open('dict.json', 'w') as openfile_object:

		print "We know the birthdays of: " 
		print [name for name in birthdays]

		user_input = raw_input("Who's birthday would you like to know? ")


		if user_input in birthdays:
			print "%s's birthday is on %s" %(user_input, birthdays[user_input])
		else:
			print "wrong input"

		print "Enter one that you would like to add to the list: "
		name = raw_input("Enter name: ")
		birthday = raw_input("Enter bithday (mm/dd/yyyy): ")
		birthdays.update({name : birthday})

		json.dump(birthdays, openfile_object)
		print birthdays





