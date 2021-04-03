# Scraper used to get job offers number from pracuj.pl

import requests
from bs4 import BeautifulSoup

profession = input("Type profession: \n")
city = input("Type city: \n")
url = 'https://www.pracuj.pl/praca/'+profession+';kw/'+city+';wp?rd=0'

try:    
    r = requests.get(url)
    r_html = r.text
    
    soup = BeautifulSoup(r_html, 'html.parser')
    
    offers = soup.find('span', 'results-header__offer-count-text-number')
    print('Number of job offers for pracuj.pl is: ',offers.get_text())

except:
    print('Results not found')
