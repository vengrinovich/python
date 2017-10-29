"""Use the BeautifulSoup and requests Python packages to print out a list of 
all the article titles on the New York Times homepage and save it to a text file."""

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

heading = soup.find_all("h2",{"class": "story-heading"})

with open('ex21file.txt', 'w') as f:
	for title in heading:
		x = (title.get_text())
		f.write (x.encode('utf-8').strip())

	







