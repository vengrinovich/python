#Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def print_horiz_line():
    print(" ---" * board_size)

def print_vert_line():
    print("|   " * (board_size + 1))

if __name__ == "__main__":
		board_size = int(input("What size of game board? "))

for index in range(board_size):
	print_horiz_line()
	print_vert_line()
print_horiz_line()
