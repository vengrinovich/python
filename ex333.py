import json
import datetime

# gets the json data from dict and loads into variable birthday, then passes this on to function birthday_date
def dictionary():

	birthday = {}
	with open('dict.json', 'r') as openfile_object:
		birthday = json.load(openfile_object)
		months(birthday)

def months(birthday):

	dates = str(birthday.values()) #extracts the dates from dictionary
	date_module = datetime.datetime.strptime(dates,'%m-%d-%Y')

dictionary()


"""def birthday_date(birthdays):
	
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
		print birthdays"""







