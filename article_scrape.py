import requests
from bs4 import BeautifulSoup

base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
r_html = r.text
soup = BeautifulSoup(r_html)

legal = soup.find('div',{'class': 'legal-container'})
paragraphs_div = soup.find('div',{'class': 'content drop-cap'})

soup.find('div',{'class': 'component-newsletter-cta'}).decompose() # decompose gets rid of those tags - erases them;
soup.find('div',{'class': 'slideshow-container embed'}).decompose()


	for text in paragraphs_div:
		print (text.get_text())





