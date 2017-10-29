"""Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.)"""

def prime_or_not():
	number = int(raw_input("Give me a number please:"))
	if number % 2 == 0:
		print "Number you provided is a prime"
	else:
		print "Number you provided isn't a prime"
prime_or_not()


"""Method 2"""
number1 = int(raw_input("Give me a number again please:"))

def prime_or_not2(number1):
	if number1 % 2 == 0:
		print "Number you provided is a prime"
	else:
		print "Number you provided isn't a prime"

prime_or_not2(number1)
