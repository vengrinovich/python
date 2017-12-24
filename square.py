# example of how you can now use import square and use this function
# from another program

def square(num):
    return num * num
    

if __name__ == "__main__":
	num = input("Give me a number: ")
	print "Hello from: %s "  % __name__
 	print(square(num))
