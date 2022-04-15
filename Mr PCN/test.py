from bs4 import BeautifulSoup
import requests


url = 'https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/NewSearchResults.aspx?srchType=MASTER&proptype=RE&srchVal=00-42-47-27-38&srchPCN='


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
trash = ''
for row in soup.find_all('tr'):
    t_datas = row.find('td')
    try:
        trash+=t_datas.text
    except:pass
import re
# search a string starting wiht owner(s) using regex
owners = re.findall(r'Owner(.*?)\n', trash)[0][3:]
print(owners)
