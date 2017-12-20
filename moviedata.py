# create an instance of the imdb class
from imdb import IMDb
ia = IMDb()

# get a movie via a movie id
the_matrix = ia.get_movie('4537896')

# list of all available infosets that can be added to a movie objects and
# searched later, for example critics review or trivia etc.
print(ia.get_movie_infoset())

# gets the imdb rating for the matrix just prints out 8.7
#print (the_matrix['rating'])

# update the movie object with more information about critic reviews
# in this case the output is ['metascore', 'metacritic url']
ia.update(the_matrix, ['critic reviews'])
ia.update(the_matrix, ['vote details'])
ia.update(the_matrix, ['release dates'])

# show the new keys added earlier, like ['metascore', 'metacritic url'] for critic reviews
# print(the_matrix.infoset2keys['critic reviews'])

# prints out the movie metascore - 73 & the number of votes in a list split by rating number
print(the_matrix.get('metascore'))
print(the_matrix.get('number of votes'))

# gives you a whole list of release dates, like
# 'France::19 May 2002 (Cannes Film Festival)\n (premiere)', 'Canada::13 September 2002 (Toronto Film Festival)', etc
print(the_matrix.get('release dates'))