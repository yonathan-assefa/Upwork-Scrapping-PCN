from tabnanny import check
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

from database_server import addtodb, createtable, updatedb, check_address

#make the firefox browser headless
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)



pcn_numbers = ['00-42-47-28-19', '00-42-47-34-22', '00-42-47-34-21', '00-42-47-28-39', '00-42-47-28-27', '00-42-47-33-03', '00-42-47-28-22', '00-42-47-33-17', '00-42-47-33-20', '00-42-47-28-30', '00-42-47-33-09', '00-42-47-28-28', '00-42-47-28-37', '00-42-47-28-25', '00-42-47-27-49', '00-42-47-27-52', '00-42-47-33-07', '00-42-47-28-36', '00-42-47-33-22', '00-42-47-34-15', '00-42-47-33-08', '00-42-47-33-19', '00-42-47-33-13', '00-42-47-34-14', '00-42-47-27-38', '00-42-47-27-43', '00-42-47-33-15', '00-42-47-28-19', '00-42-47-34-22', '00-42-47-34-21', '00-42-47-28-39', '00-42-47-28-27', '00-42-47-33-03', '00-42-47-28-22', '00-42-47-33-17', '00-42-47-33-20', '00-42-47-28-30', '00-42-47-33-09', '00-42-47-28-28', '00-42-47-28-37', '00-42-47-28-25', '00-42-47-27-49', '00-42-47-27-52', '00-42-47-33-07', '00-42-47-28-36', '00-42-47-33-22', '00-42-47-34-15', '00-42-47-33-08', '00-42-47-33-19', '00-42-47-33-13', '00-42-47-34-14', '00-42-47-27-38', '00-42-47-27-43']

for pcn_number in pcn_numbers:
    print("Fetching data for " + pcn_number)
    browser.get(f'https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/NewSearchResults.aspx?srchType=MASTER&proptype=RE&srchVal={pcn_number}&srchPCN=')

    # selenium get element by id


    loops = (int(browser.find_element(By.XPATH, '/html/body/form/div[3]/div/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/i/b[3]').text) // 100) + 1 
    print(loops)
    for pages in range(loops):
        try:
            print("searching ...")

            # import time
            # time.sleep(5)
            # myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'txtSearch')))
            s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').click()
            s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').send_keys('100')

            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            tbs = soup.find("table", {"id": "gvSrchResults"})
            for td in tbs.find_all("td", {"style": "width:28%;"}):
                address = td.text.strip()
                print(address)
                # exists = check_address(address)
                # print(exists)
                # addtodb(td.text)


        except:
            print("some")