#Learning directly from the one and only geeksforgeeks
#https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

#Installed External Libraries
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup

URL = "https://cardfight.fandom.com/wiki/Booster_Set_1:_Descent_of_the_King_of_Knights"
pageRequest = requests.get(URL)

#print(pageRequest.content)

parsedContent = BeautifulSoup(pageRequest.content, 'html5lib')
#print(parsedContent.prettify())

table = parsedContent.find('table')

#print(table)

cardList = table.find_all('tr')
#print(cardList)

for row in cardList:
    #print(row)
    secondRow = row.find_all('td')
    #print("hi")

    if (secondRow != []):
        print(secondRow[1].find('a').get('href'))

#for link in table.find_all('a'):
    #print(link.get('href'))