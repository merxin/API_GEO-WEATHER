import requests, datetime as dt, calendar
URL_WEATHER = 'http://api.openweathermap.org/data/2.5/onecall'
API_WEATHER = 'YOUR OPENWEATHER API'
API_CITY = 'YOUR API_NINJAS GEOCODING API'
URL_CITY = 'https://api.api-ninjas.com/v1/geocoding'

try:

    city = input('which city would you like to get your forecast for? ')
    country_code = input('Enter country ')
    parameters ={'city':city, 'country':country_code}
    horizon = int(input('Please enter horizon of your forecast (1-7 days): '))
    response1 = requests.get(URL_CITY, params=(parameters), headers={'X-Api-Key': API_CITY})
    lat = (response1.json()[0]['latitude'])
    lon = (response1.json()[0]['longitude'])

    weather_params = {'lat': lat,
                      'lon': lon,
                      'city_name': city,
                      'appid': API_WEATHER}

    print(city, 'lat: ', lat, 'lon: ', lon)
    assert horizon in [1, 2, 3, 4, 5, 6, 7], 'Please enter a number between 1 and 7'
    response = requests.get(URL_WEATHER, params=weather_params)
    print('Day'.ljust(20)[:20], "Temperature in C".ljust(20)[:20], "Weather description")
    for i in range(0, horizon):
        formatted_day = calendar.day_name[(dt.date.today() + dt.timedelta(days=i)).weekday()]
        print(formatted_day.ljust(20)[:20], str(int(response.json()['daily'][i]['temp']['max']) - 273).ljust(20)[:20],
              response.json()['daily'][i]['weather'][0]['description'])
except IndexError:
    print('Enter valid city/country name')
except AssertionError as e:
    print(e)



