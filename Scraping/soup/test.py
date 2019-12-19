import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html5lib')
#print(soup.prettify())
quote = soup.find('div',attrs={'class':'quote'})
q = quote.findAll('span',attrs={'class':'text'})
print(q.preetify())
author = quote.findAll('small',attrs={'class':'author'})
print(author)
tags = quote.findAll('div',attrs={'class':'tags'})
print(tags)
