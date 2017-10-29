import random

def cows_bulls():
	guesses = 0
	number_list = (str(random.randint(0,9999)).zfill(4))
	print number_list

	while True:
		user_input = str(raw_input("Enter a 4 digit number: "))
		bulls = []
		cows = []
		guesses += 1
		if user_input[0] == number_list[0]:
			bulls.append(number_list[0])
		elif number_list[0] in user_input:
			cows.append(number_list[0]) 
		if user_input[1] == number_list[1]:
			bulls.append(number_list[1])
		elif number_list[1] in user_input:
			cows.append(number_list[1]) 
		if user_input[2] == number_list[2]:
			bulls.append(number_list[2])
		elif number_list[2] in user_input:
			cows.append(number_list[2]) 
		if user_input[3] == number_list[3]:
			bulls.append(number_list[3])
		elif number_list[3] in user_input:
			cows.append(number_list[3])
		if number_list == user_input:
			print 'you have %d bulls and %d cows using %d guesses' % (len(bulls), len(cows), guesses)
			break
		print 'you have %d bulls and %d cows' % (len(bulls), len(cows))














	




	



