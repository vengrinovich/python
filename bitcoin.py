import requests
from bs4 import BeautifulSoup

base_url = 'https://www.worldcoinindex.com/coin/bitcoin'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

current_price = soup.find('div',{'class': 'col-md-6 col-xs-6 coinprice'})

print current_price