STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_stock_api"
NEWS_API_KEY = "your_news_api"

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

TWILIO_ACC_SID = 'your_twilio_acc_sid'
TWILIO_ACC_AUTH_TOKEN = 'your_twilio_acc_auth_token'
TWILIO_FROM_NUM = 'your_twilio_virtual_num'
TWILIO_TO_NUM = 'receiver_num'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests
from twilio.rest import Client

parameters = {
    "function":"TIME_SERIES_DAILY",
    'symbol':STOCK,
    'apikey':STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)

data = response.json()['Time Series (Daily)']

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]

yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]

day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']

# print(yesterday_closing_price, day_before_yesterday_data_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference/float(yesterday_closing_price))*100)

print(diff_percent)

if abs(diff_percent) > 1:

    ## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_parameters = {
        'apiKey':NEWS_API_KEY,
        'qInTitle':COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

    news_articles = news_response.json()['articles']

    three_articles = news_articles[:3]

    print(three_articles)

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number. 

    formated_articles = [f"{COMPANY_NAME}: {up_down} {diff_percent}%. \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_ACC_SID, TWILIO_ACC_AUTH_TOKEN)

    for article in formated_articles:
        message = client.messages.create(
            body=article, from_=TWILIO_FROM_NUM, to=TWILIO_TO_NUM
            )
