"""Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks 
for a new password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, 
pick a word or two from a list."""

import random, string 

def password_generator():
	WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
	strength = raw_input("How strong do you want your password to be? (easy/medium/hard):\n")
	a = []
	lowercase = string.ascii_lowercase
	uppercase = string.ascii_uppercase
	digits = string.digits
	symbols = string.punctuation
	everything = lowercase + uppercase + digits + symbols

	if strength == 'hard':
		size = int(raw_input("How lengthy should your password be?:\n"))
		for x in range(0, size):
			choice = (random.choice(everything))
			a.append(choice)
			
		final_password = ''.join(a)
		return final_password
	
	elif strength == 'medium':
		medium_password = ''.join(random.sample(WORDS,2) + random.sample(digits,1))
		return medium_password
	
	elif strength == 'easy':
		easy_password = ''.join(random.sample(WORDS,1) + random.sample(digits,1))
		return easy_password

print(password_generator())






