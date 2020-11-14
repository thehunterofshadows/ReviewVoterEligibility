import re
import time
from datetime import datetime
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

#configurations
staticSite = "https://www.echovita.com/us/obituaries/wi/milwaukee"

#functions required to pull the data
def get_website(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #page = urlopen(req).read()
    page = open("milwaukee.html").read()
    soup=bs(page,"html.parser")
    return soup

def get_date_website(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    #page = open("milwaukee.html").read()
    soup=bs(page,"html.parser")
    return soup

def get_single_obt_url(endPiece):
    return "".join(['https://www.echovita.com',endPiece])
#main code

def pull_passed_people(siteData):
    return siteData.find_all(attrs={'class' : re.compile('^text-name-obit-in-list text-color-default')})

def pull_dates(siteData):
    y=0
    results = siteData.find_all(attrs={'class' : re.compile('^mt-2 mb-1 text-white font-weight-bold text-shadow-darker fs-18 lh-27')})
    print(results[0].text)



siteData = get_website(staticSite)
limitRuns = 0
for div in pull_passed_people(siteData):
    limitRuns = limitRuns +1
    print(limitRuns)
    pull_dates(
        get_date_website(
            get_single_obt_url(div['href'])))

    #print(div['href'])
    #print(get_single_obt_url(div['href']))
    if limitRuns >3:
        break
print("done")
