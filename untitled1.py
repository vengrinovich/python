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