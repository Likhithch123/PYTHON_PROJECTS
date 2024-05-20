from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time

def working_function():
    cookie_money = driver.find_element(By.ID, value='money').text
    cookie_money = int(cookie_money)

    cursor_price_element = driver.find_element(By.CSS_SELECTOR, value='#buyCursor b')
    cursor_price_list = cursor_price_element.text.split()
    cursor_price = cursor_price_list[-1]
    cursor_price = int(cursor_price)

    grandma_price_element = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
    grandma_price_list = grandma_price_element.text.split()
    grandma_price = grandma_price_list[-1]
    grandma_price = int(grandma_price)

    factory_price_element = driver.find_element(By.CSS_SELECTOR, value='#buyFactory b')
    factory_price_list = factory_price_element.text.split()
    factory_price = factory_price_list[-1]
    factory_price = int(factory_price)

    if cookie_money >= factory_price:
        driver.find_element(By.CSS_SELECTOR, value='#buyFactory').click()
    elif cookie_money >= grandma_price:
        driver.find_element(By.CSS_SELECTOR, value='#buyGrandma').click()
    elif cookie_money >= cursor_price:
        driver.find_element(By.CSS_SELECTOR, value='#buyCursor').click()
    else:
        pass


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie_obj = driver.find_element(By.ID, value='cookie')

time_out = time() + 5
five_min = time() + 60*5

while True:
    cookie_obj.click()
    if time() > time_out:
        working_function()
        time_out = time() + 5
    if time() > five_min:
        cookie_count = driver.find_element(By.ID, value='cps').text
        print(cookie_count)
        break

driver.quit()