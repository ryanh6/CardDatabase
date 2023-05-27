#Learning directly from the one and only geeksforgeeks
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

import requests
from bs4 import BeautifulSoup

URL = "https://www.google.ca/"
pageRequest = requests.get(URL)

#print(pageRequest.content)

soup = BeautifulSoup(pageRequest.content, 'html5lib')
print(soup.prettify())