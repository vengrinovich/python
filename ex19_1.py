import requests
from bs4 import BeautifulSoup

def print_text(base_url):
	r = requests.get(base_url)
	r_html = r.text
	soup = BeautifulSoup(r_html)

	article_body = soup.find('div',{'id': 'article_body'})
	paragraphs = article_body.find_all('p')

	for text in paragraphs:
		print text.get_text()

url = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749.html'
url_page_2 = 'http://www.washingtonpost.com/wp-dyn/content/article/2010/08/29/AR2010082902749_2.html?sid=ST2010082902923'
print print_text(url)
print print_text(url_page_2)