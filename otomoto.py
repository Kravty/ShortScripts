# Scraper used for getting information from otomoto - Polish car sales portal.
# Output is number of car offers and data from first offer.

import requests
from bs4 import BeautifulSoup


print('Program displays number of car offers from otomoto for given specification. \
\n' +'Type enter to skip parameter')

brand = input('Type brand:\n') + '/'
model = input('Type model:\n') + '/'
min_year = input('Minimal year:\n') + '/'
city = input('Type city:\n') + '/'

try:
    response = requests.get('https://www.otomoto.pl/osobowe/' + brand+model + '/od-' + min_year+city)
    response_html = response.text
    
    soup = BeautifulSoup(response_html, 'html.parser')
    
    offers_number = soup.find('span', 'counter').get_text()
    specification = soup.find('ul', 'ds-params-block').get_text()
    price = soup.find('span', 'offer-price__number').get_text()
    
    print('Number of offers for such specification', offers_number, 
    '\n'+'First car offer specification:', specification, '\nPrice:', price)

except:
    print('Results not found.')
