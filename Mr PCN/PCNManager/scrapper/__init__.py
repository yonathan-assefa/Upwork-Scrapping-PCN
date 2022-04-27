from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)