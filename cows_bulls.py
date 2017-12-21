"""Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over.
source - http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html"""

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


if __name__ == "__main__":
	print(cows_bulls())












	




	



