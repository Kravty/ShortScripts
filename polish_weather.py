# Program prints actual temperature for given Polish city using API

import requests as r

city = input('Type city:\n')

try:
    response = r.get('http://api.openweathermap.org/data/2.5/weather?q='+city+',pl&appid=524fd3d7bec2274ae22c9d6a4540f3f9')
    json = response.json()
    
    print('Actual temperature for city', city, 'is', str(round(json['main']['temp']-273.15,1))+'°C')
    print('Feels like temperature for city', city, 'is', str(round(json['main']['feels_like']-273.15,1))+'°C')

except:
    print('Results not found.')
