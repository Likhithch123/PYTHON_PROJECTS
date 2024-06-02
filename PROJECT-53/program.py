# Tested with the following package versions:
# beautifulsoup4==4.12.3
# Requests==2.31.0
# selenium==4.21.0

ZILLOW_CLONE_URL = 'https://appbrewery.github.io/Zillow-Clone/'

# Part 1 - Scrape the links, addresses, and prices of the rental properties

import requests
from bs4 import BeautifulSoup
from os import environ

# Used our Zillow-Clone website (instead of Zillow.com)
zillow_web_page = requests.get(ZILLOW_CLONE_URL)
response = BeautifulSoup(zillow_web_page.text,'html.parser')

result_of_prices = response.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine')
list_of_prices = [price_tag.getText().replace('/mo','').split('+')[0] for price_tag in result_of_prices]

result_of_links = response.find_all(name='a',class_='property-card-link')
list_of_links = [tag.get('href') for tag in result_of_links]

result_of_addresses = response.find_all(name='address')
list_of_addresses = [address.getText().strip().replace(' | ',' ') for address in result_of_addresses]
final_list_of_addresses = [address.replace('#','') for address in list_of_addresses]

# Part 2 - Fill in the Google Form using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
bot = webdriver.Chrome(options=chrome_options)

for n in range(len(list_of_links)):
    
    bot.get(environ.get('google_form_address'))
    sleep(2)

    address_input = bot.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = bot.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = bot.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = bot.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address_input.send_keys(final_list_of_addresses[n])
    price_input.send_keys(list_of_prices[n])
    link_input.send_keys(list_of_links[n])
    submit_button.click()

bot.quit()