"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Extras:

1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""


number = int(raw_input("Enter a number please:"))

if number % 4 == 0:
	print "this number is a multiple of 4"
elif number % 2 == 0:
	print "Congrats, %d is an even number" % number
else:
	print "%d is not an even number" % number 

number1 = int(raw_input("Enter another number:"))
number2 = int(raw_input("Enter yet another number please:"))

if number2 % number1 == 0:
	print "%d evenly divides by %d" % (number2,number1)
else:
	print "%d does not evenly divide by %d" % (number2,number1)


