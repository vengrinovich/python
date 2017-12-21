"""Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, 
except with the words in backwards order. """

  

def reverse(string):
	list1 = string.split()
	list2 = list1[::-1]
	result = " ".join(list2)
	return result

def prompt():
	string = raw_input("Please type in a centence: \n")
	print reverse(string)

prompt()
