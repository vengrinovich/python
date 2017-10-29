"""Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can use functions. 
ke sure to ask the user to enter the number of numbers in the sequence to generate."""

def fibonacci(num):
	num1 = int(num)
	x = 1
    	if num1 == 0:
        	fib = []
    	elif num1 == 1:
        	fib = [1]
    	elif num1 == 2:
        	fib = [1,1]
    	elif num1 > 2:
        	fib = [1,1]
        	while x < (num1 - 1):
            		fib.append(fib[x] + fib[x-1])
            		x += 1

    	return fib
    	
def input():
	num = int(raw_input("How many numbers in your sequence?"))
	print(fibonacci(num))

input()


	





