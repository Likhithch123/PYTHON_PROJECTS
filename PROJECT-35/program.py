API_KEY = 'your_api_key'
LAT = "your_latitude"
LONG = "your_longitude"

import requests
from twilio.rest import Client

account_sid = "your_account_client"
auth_token = "your_auth_token_clinet"
client = Client(account_sid, auth_token)


parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'cnt': 4,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', parameters)

response.raise_for_status()

print(f'Status code:{response.status_code}')

weather_data = response.json()

next_12_hours_forecast = []

for i in range(parameters['cnt']):
    condition_code = weather_data['list'][i]['weather'][0]['id']  
    next_12_hours_forecast.append(condition_code)

print(next_12_hours_forecast)

for condition_codes in next_12_hours_forecast:
    if condition_codes < 700:
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☂️.",
            from_='senders_number',
            to='receiver_number'
        )

        print(message.status)
        break