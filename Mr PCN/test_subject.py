from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import time
import re
import requests

browser = webdriver.Firefox()

browser.get('https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel=00424728270021604&srchtype=MASTER&srchVal=00-42-47-28-27')




soup = BeautifulSoup(browser.page_source, 'html.parser')

sc_list = []
tbs = soup.find_all("table", {'width':'100%', 'cellspacing':'0', 'cellpadding':'1'})
for i in tbs:
    for m in i.find_all('tr'):
        for j in m.find_all('td', {'class': 'TDValueLeft', 'colspan': '2'}):
            sc_list.append(j.text)

x = []
for i in sc_list:
    if i.startswith('\n'):
        break
    else:
        x.append(i)
print(x)
