from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#make the firefox browser headless
options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
browser = webdriver.Firefox()



browser.get('https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/NewSearchResults.aspx?srchType=MASTER&proptype=RE&srchVal=00-42-47-27-38&srchPCN=')

# selenium get element by id



print("search.text")
# import time
# time.sleep(5)
# myElem = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'txtSearch')))

# search = browser.find_element(By.CLASS_NAME,'txtSearch').click()
s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').click()
s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').send_keys('100')
# search.click()
# for option in s100:
#     if option.text == '100':
#         option.click() # select() in earlier versions of webdriver
#         break
browser.get('https://www.pbcgov.org/papa')

print("search.text")