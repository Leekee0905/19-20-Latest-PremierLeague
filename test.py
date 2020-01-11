import requests
from bs4 import BeautifulSoup
import re
url = ('https://www.premierleague.com/tables')

rank = requests.get(url)
soup = BeautifulSoup(rank.content,'html.parser')

team_rank = soup.select('tbody>tr')
team_rank_wds = soup.find_all('td')

for num in range (1,40,2):
    a=team_rank[num]
    for num2 in range (2,11):
        print(team_rank_wds[num2])[num]