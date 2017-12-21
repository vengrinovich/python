"""Make a two-player Rock-Paper-Scissors game."""

import random
words = ['rock', 'paper', 'scissors']

def function():

	while True:
		word = random.choice(words)
		input = raw_input("Pick rock, paper, or scissors:")
		print "the computer picked %s" % word
		if input == 'rock' and word == 'scissors':
			print "You won, would you like to play again?"
			new_input = raw_input("Yes or No:")
			if new_input == 'yes':
				return function()
			else:
				break
		elif input == 'scissors' and word == 'paper':
			print "You won, would you like to play again?"
			new_input = raw_input("Yes or No:")
			if new_input == 'yes':
				return function()
			else:
				break
		elif input == 'paper' and word == 'rock':
			print "You won, would you like to play again?"
			new_input = raw_input("Yes or No:")
			if new_input == 'yes':
				return function()
			else:
				break
		elif input == word:
			print "It's a draw, would you like to play again?"
			new_input = raw_input("Yes or No:")
			if new_input == 'yes':
				return function()
			else:
				break
		elif input != 'rock' and input != 'paper' and input != 'scissors':
			print "This is not an appropriate value, pick again"
			return function()
		else:
			print "You lost, would you like to play again?"
			new_input = raw_input("Yes or No:")
			if new_input == 'yes':
				return function()
			else:
				break

function()











