#Learning directly from the one and only geeksforgeeks
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

import requests

URL = "https://www.google.ca/"
pageRequest = requests.get(URL)

print(pageRequest.content)

#for word in range(10):
    #print(str(pageRequest.content[word]))