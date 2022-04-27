from django.shortcuts import redirect, render
from django.views.generic import View

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import re
import requests

# load variables from __init__.py
from scrapper import browser

from .forms import PCNForm
from .models import PCN


def clean_data(pcn_number, pcn_file):
    """
    Clean data from form
    """
    pcn = pcn_number
    pcn_file = pcn_file
    
    pcn_list = []

    
    # read pcn_file and get pcn list
    if pcn_file:
        with open(pcn_file, 'r') as f:
            pcn_list = f.read().splitlines()
    if pcn:
        pcn_list.append(pcn)
    
    # check if each pcn list is unique
    pcn_list = list(set(pcn_list))

    return pcn_list

def home(request):
    return render(request, "home.html")

def scrap_data(pcn_list):
    pcn_numbers = pcn_list
    for pcn_number in pcn_numbers:
        print("Fetching data for " + pcn_number)
        browser.get(f'https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/NewSearchResults.aspx?srchType=MASTER&proptype=RE&srchVal={pcn_number}&srchPCN=')


        loops = (int(browser.find_element(By.XPATH, '/html/body/form/div[3]/div/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/i/b[3]').text) // 100) + 1 
        for pages in range(loops):
            try:
                print("search.text")
                s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').click()
                s100 = browser.find_element(By.NAME, 'ctl00$MainContent$ddlPgSizeTop').send_keys('100')

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

                    sc_list = []
                    tbs = soup.find_all("table", {'width':'100%', 'cellspacing':'0', 'cellpadding':'1'})
                    for i in tbs:
                        for m in i.find_all('tr'):
                            for j in m.find_all('td', {'class': 'TDValueLeft', 'colspan': '2'}):
                                sc_list.append(j.text)

                    owners_name = []
                    for i in sc_list:
                        if i.startswith('\n'):
                            break
                        else:
                            owners_name.append(i)
                    for owner_name in owners_name:
                        # save the data to the PCN table
                        PCN.objects.create(
                            pcn = pcn,
                            owner = owner_name,
                            location = location_address,
                            subdivision = subdivision,
                            legal_description = legal_description,
                            control_number = pc_num
                        ).save()
                        
                for pc_nums in sc_list:
                    get_user_info(pc_nums)

                browser.find_element(By.PARTIAL_LINK_TEXT,value="Next").click()
            except:
                print("Something went wrong")



class ScrapView(View):
    template_name = 'index.html'
    success_url = 'home'

    def get(self, request):
        form = PCNForm(request.POST or None, request.FILES or None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PCNForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data
            pcn = form.get('pcn')
            pcn_file = form.get('pcn_file')
            pcn_list = clean_data(pcn, pcn_file)
            print(pcn_list)
            scrap_data(pcn_list)
        form = PCNForm(request.POST, request.FILES)
        return render(request, self.template_name, {'form': form})



