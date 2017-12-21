"""Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
Print out that many copies of the previous message on separate lines. """


while True:
	try:
		print "Enter your age:",
		age = int(raw_input())
		print "Give me a number",
		number = int(raw_input())
	except ValueError:
		print "This is not an integer"
	else: 
		break

print "What's your name then?",
name = raw_input()
age_till_100 = 100 - age
x = 0

while x != number:
	print "\tWell, well, well, %s, in %d years you will be 100 lears old\n" % (name, age_till_100)
	x = x + 1
	 
