
import zipfile # to open and manipulate zip files & their contents
from itertools import product

def open_zip_file():
	
	filename = raw_input("Enter the name of the zip file: ")
	zip_file = zipfile.ZipFile(filename) # to open a zip file
	brute_force_attack(zip_file)

def open_dict_file():

	filename = raw_input("Enter the name of the zip file: ")
	dict_name = raw_input("Enter the dictionary name: ")

	zip_file = zipfile.ZipFile(filename)
	
	with open (dict_name, 'r') as open_dict_object:
		dictionary = open_dict_object.read()

	dictionary_attack(zip_file, dictionary)
	
def dictionary_attack(filename, dict_file):

	dict_file = dict_file.split() # puts everything into a list with comma separated values

	for word in dict_file:
		try:
			filename.extractall(pwd=word.encode())
			print True
			print word
			return word
			return True
		except:
			pass

def brute_force_attack(filename):
	
	# extra: namelist list contents of the zipfile like ex1.py
	not_used = ([name for name in filename.namelist()])

	#extractall applies a password to the open zip file to extract all of it's members	
	#product generates tuples of charachters like ('a','b','c' etc.) and then repeats them any number
	#of times like ('aa','ab','ac' etc.); after we join them together in a string aa or ab etc.	
	for i in range(8):
		for items in product('abcdefghijklmnopqrstuvwxyz',repeat=i):
    			variable = ''.join(items)
    			try: 
    				filename.extractall(pwd=variable.encode())
    				print True
    				print variable
    				return variable # return stops the loop into going further
    			except:
    				pass #all error values are ignored


if __name__ == '__main__':
	choice = raw_input("brute force, dictionary or lower: ")

	if choice == 'dictionary':
		open_dict_file()
	elif choice == 'brute force':
		open_zip_file()
	elif choice == 'both':
		open_dict_file()
		open_zip_file()
