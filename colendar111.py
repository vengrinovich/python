"""build a basic calendar that the user will be able to interact with from the command line. 
The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
Let's begin!"""


from time import sleep, strftime

calendar = {}

def welcome():
	print "Welcome, user, the calendar is opening"
	print "the current date is: %s" % strftime('%a, %d %b %Y')
	print "the current time is: %s" % strftime('%H:%M:%S')
	print "what would you like to do?"

def start_calendar():
	welcome()

	start = True
	
	while start:
		user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit:")
		user_choice = user_choice.upper()

		if user_choice == 'V':
			if len(calendar) == 0:
				print "The calendar is empty"
			else:
				print calendar
		
		elif user_choice == 'U':
			date = raw_input("What date?")
			event = raw_input("Enter the update: ")
			calendar.update({event : date})
			print "Update successful"
		
		elif user_choice == 'A':
			event = raw_input("Enter event: ")
			date = raw_input("Enter date (MM/DD/YYYY): ")
			
			if len(date) != 10 or int(date[6:10]) < int(strftime('%Y')):
				try_again = raw_input("an invalid date was entered, would you like to try again? Y for yes, N for No: ")
				try_again = try_again.upper()
				if try_again == 'Y':
					continue
				else:
					start = False
			else:
				calendar.update({event : date})
				print "Event was succesfully added"
		
		elif user_choice == 'D':
			if len(calendar) == 0:
				print "The calendar is empty"
			else:
				event = raw_input("Enter event: ")
				if event in calendar.keys():
					del calendar[event]
					print "Event successfully deleted"
			

		elif user_choice == 'X':
			print calendar
			start = False
		
		else:
			print "Invalid command was added"

start_calendar()

