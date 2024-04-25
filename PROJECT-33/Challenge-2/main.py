import requests, datetime, smtplib, time

MY_LAT = 'your_latitude'
MY_LNG = 'your_longitude'

MY_EMAIL = 'your_email'
MY_PASSWORD = 'your_app_password'

def is_iss_overhead():
    response1 = requests.get('http://api.open-notify.org/iss-now.json')
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude = float(data1['iss_position']['latitude'])
    iss_longitude = float(data1['iss_position']['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {'lat': MY_LAT, 'lng': MY_LNG, 'formatted': 0}

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    today = datetime.datetime.now()

    sunrise_time = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_time = int(data['results']['sunset'].split('T')[1].split(':')[0])

    if today.hour <= sunrise_time or today.hour >= sunset_time:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, msg='Subject: Look Up\n\nThe ISS is above you in the sky.')
