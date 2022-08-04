from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
# make chrome headless
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# browser withou webdrivermanager
# browser = webdriver.Firefox(options=options)

