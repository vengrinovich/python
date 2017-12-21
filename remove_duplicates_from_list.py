"""Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates."""


import random

def list_random(val,val1):
	list1 = [random.choice(range(val1)) for i in range(val)]
	print "This is your original set: %s" % list1
	print remove_duplicates(list1)

def prompt():
	val = int(raw_input("How long would yu like your list to be? "))
	val1 = int(raw_input("What would you like the range to be?"))
	print list_random(val,val1)

def remove_duplicates(list1):
	print "this is your list with no duplicates: "
	return set(list1)
  
prompt()

