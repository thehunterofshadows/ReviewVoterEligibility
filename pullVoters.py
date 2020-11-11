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


#main code

siteData = get_website(staticSite)
for div in siteData.find_all(attrs={'class' : re.compile('^text-name-obit-in-list text-color-default')}):
    print(div['href'])
