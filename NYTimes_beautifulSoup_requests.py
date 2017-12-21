"""Use the BeautifulSoup and requests Python packages to print out a list of 
all the article titles on the New York Times homepage. """

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

heading = soup.find_all("h2",{"class": "story-heading"})

for title in heading:
	x = (title.get_text())
	print x.strip()

	







