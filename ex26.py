game = [[2, 1, 1],
		[1, 1, 0],
		[1, 0, 2]]

if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][0]:
	print "diagonal" 
elif game[0][0] == game[1][0] == game[2][0] or game[0][1] == game[1][1] == game[2][1] or game[0][2] == game[1][2] == game[2][2]:
	print "vertical"
for x in game:
	if x[0] == x[1] == x[2]:
		print "accross"

	


	
