game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

def check_winner(game):
	if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
		print "diagonal" 
	elif game[0][0] == game[1][0] == game[2][0] or game[0][1] == game[1][1] == game[2][1] or game[0][2] == game[1][2] == game[2][2]:
		print "vertical"
	for x in game:
		if x[0] == x[1] == x[2]:
			print "accross"

for x in range(9):
	player1_raw = int(raw_input("enter row number: "))
	player1_column = int(raw_input("enter column number: "))

	game[player1_raw-1][player1_column-1] = 'X'
	print game

	player2_raw = int(raw_input("enter row number: "))
	player2_column = int(raw_input("enter column number: "))

	game[player2_raw-1][player2_column-1] = 'O'
	print game
	check_winner(game)




