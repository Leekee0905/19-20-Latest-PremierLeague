import requests
from bs4 import BeautifulSoup

url = ('https://www.premierleague.com/tables')

rank = requests.get(url)
print(rank.content)
soup = BeautifulSoup(rank.content,'html.parser')

team_rank_wds = soup.select('tbody>tr')

for team_rank_wds in range(0,40,2):