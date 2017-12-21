"""Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)"""

string = raw_input("Provide a word:")
string_reverse = string[::-1]

if string == string_reverse:
	print "This word is a palindrome"
else:
	print "This one isn't"



