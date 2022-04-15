from urllib import response
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# send request to the web page with bs4
def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')



# find element in bs4
main_url = 'https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/NewSearchResults.aspx?srchType=MASTER&proptype=RE&srchVal=00-42-47-27-38&srchPCN='
each_url = 'https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel=00424727380000870&srchtype=MASTER&srchVal=00-42-47-27-38'

response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())


# bs4 iterate through the table each row having class name
# and print the data

sc_list = []

for row in soup.find_all('tr', class_='gridrow2'):
    t_datas = row.find_all('td')
    sc_list.append(t_datas[3].text)

for row in soup.find_all('tr', class_='gridrowalternate2'):
    t_datas = row.find_all('td')
    sc_list.append(t_datas[3].text)


