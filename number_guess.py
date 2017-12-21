import random
a = random.randint(1,9)
guesses = 0

while True:
	user_number = raw_input("Please guess a number from 1 to 9:")
	if user_number == 'exit':
		break
	elif int(user_number) == a:
		guesses += 1
		print "You guessed it right using %d guesses" % guesses 
		break
	elif int(user_number) > a:
		guesses += 1
		print "Your number is higher then computer's, try again"
	elif int(user_number) < a:
		guesses += 1
		print "Your number is lower then computer's, try again"
	

