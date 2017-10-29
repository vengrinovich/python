#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
#and print out the results to the screen.

"""with open('nameslist.txt', 'r') as open_file_object:
	all_words = open_file_object.read()
	
	x = all_words.split() # puts words in a list and separates with a comma

	print len(x) #length of all words in nameslist.txt
	print len(set(x)) # number of unique words in the dataset"""

#method 2
with open("nameslist.txt") as names:
	test = {}
	line = names.read()
	for name in line.split('\n'):
		if name in test:
			test[name] += 1
		else:
			test[name] = 1 
	print len(test)



	


	


	



