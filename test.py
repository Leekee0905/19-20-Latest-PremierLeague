import requests
from bs4 import BeautifulSoup
import re
url = ('https://www.premierleague.com/tables')

rank = requests.get(url)
soup = BeautifulSoup(rank.content,'html.parser')

team_rank = soup.select('tbody>tr')

for num in range (1,40,2):
    a=team_rank[num]
    b=a.find_all('td')
    for num2 in range (2,11):
        print(b[num2])
