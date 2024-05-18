import smtplib
import requests
from bs4 import BeautifulSoup

PRODUCT_URL = 'url_of_your_amazon_product'

EMAIL = 'your email id'
PASSWORD = 'your google app password'


headers = {
    'User-Agent' : 'your browser user-agent',
    'Accept-Language':'your browser accept language',
}

response = requests.get(PRODUCT_URL, headers = headers)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

actual_price = soup.find(name='span',class_='a-offscreen').getText().split('₹')[1].replace(',','')

target_price = input('Enter the price of the product that you wish to buy for: ')

target_price_as_float = float(target_price)
actual_price_as_float = float(actual_price)

subject_line_mail = 'Amazon Price Alert!'
title_of_the_product = soup.find(name='span',id='productTitle').getText().strip()

if target_price_as_float >= actual_price_as_float:
    with smtplib.SMTP('your smtp address', port='port number that matches your smtp address') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f'Subject: {subject_line_mail}\n\n{title_of_the_product} is now available for{actual_price_as_float}.')
