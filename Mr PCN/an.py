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

from database_server import addtodb, createtable, updatedb

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
    for pages in range(loops):
        try:
            print("search.text")

            # import time
            # time.sleep(5)
            # myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'txtSearch')))
            s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').click()
            s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').send_keys('100')

            # browser.find_element(By.PARTIAL_LINK_TEXT,value="Next").click()
            # search = browser.find_element(By.CLASS_NAME,'txtSearch').click()
            # search.click()
            # for option in s100:
            #     if option.text == '100':
            #         option.click() # select() in earlier versions of webdriver
            #         break


            time.sleep(3)

            soup = BeautifulSoup(browser.page_source, 'html.parser')

            sc_list = []

            for row in soup.find_all('tr', class_='gridrow2'):
                t_datas = row.find_all('td')
                sc_list.append(t_datas[3].text)

            for row in soup.find_all('tr', class_='gridrowalternate2'):
                t_datas = row.find_all('td')
                sc_list.append(t_datas[3].text)

            def get_user_info(pc_num):
                each_url = f'https://www.pbcgov.org/papa/Asps/PropertyDetail/PropertyDetail.aspx?parcel={pc_num}&srchtype=MASTER&srchVal=00-42-47-27-38'
                response = requests.get(each_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                # find specific id
                location_address = soup.find('span', id='MainContent_lblLocation').text
                pcn = soup.find('span', id='MainContent_lblPCN').text
                subdivision = soup.find('span', id='MainContent_lblSubdiv').text
                legal_description = soup.find('span', id='MainContent_lblLegalDesc').text

                trash = ''
                for row in soup.find_all('tr'):
                    t_datas = row.find('td')
                    try:
                        trash+=t_datas.text
                    except:pass
                # search a string starting wiht owner(s) using regex
                owner_name = re.findall(r'Owner(.*?)\n', trash)[0][3:]
                userInfo = {
                    'location_address': location_address,
                    'pcn': pcn,
                    'subdivision': subdivision,
                    'legal_description': legal_description,
                    'owner_name': owner_name
                }
                addtodb(userInfo=userInfo)


            for pc_nums in sc_list:
                get_user_info(pc_nums)

            browser.find_element(By.PARTIAL_LINK_TEXT,value="Next").click()
        except:
            print("Something went wrong")



