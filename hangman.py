#In this exercise, the task is to write a function that picks a random word 
#from a list of words from the SOWPODS dictionary.

#For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
#For now, let the player guess an infinite number of times until they get the entire word. 
#As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again""".

import random

def generate_word(filename):

	with open (filename,'r') as file_object:
		words = file_object.read().split()
		random_word = random.choice(words)
		print random_word
		guess_word(random_word)

def draw_hangman(guesses):
		values = ['O', ' O \n/', ' O \n/|', ' O \n/|\ ', ' O \n/|\ \n | ', 
		' O \n/|\ \n | \n/ ', ' O \n/|\ \n | \n/ \ '] 
		print values[guesses]

def guess_word(word):

	guessed = ''
	word = list(word)
	current_guess = '_' * len(word)
	current_guess = list(current_guess)
	num_guesses = 0
		
	while num_guesses != 6:
		user_letter = raw_input("Guess a letter: ")

		if user_letter in guessed:
			print "Already guessed that one, try again"

		elif user_letter not in word:
			guessed += user_letter
			num_guesses += 1
			print "Incorrect, try again, you have %d incorrect gueeses" % num_guesses
			draw(num_guesses)	

		while user_letter in word: # while takes care of a case where a letter is present in the word more then once
			index = word.index(user_letter) #get's the position of user letter in the actual word
			current_guess[index] = user_letter # puts the user letter in the same position as it is in the actual word
			word[index] = '_' # makes sure that the letter that has been guessed is removed so it's not referenced again
			guessed += user_letter
		print current_guess

	new_game =  raw_input("You lost, Would you like to start a new game? 'Y' or 'No'?")

	if new_game == 'Y':
		print generate_word('sowpods.txt')
	else:
		print "Thanks for playing, loser"

generate_word('sowpods.txt')






