import random

def my_list():
	list = random.sample(range(200), 10)
	print "this is the current list: %s" % list
	first = list[0]
	last = list[-1]

	print "This is the first number: %s" % first
	print "This is the last number: %s" % last

my_list()







