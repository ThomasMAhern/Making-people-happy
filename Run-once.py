pip install selenium
pip install beautifulsoup4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from lxml import html
import requests
from bs4 import BeautifulSoup

# creating a function for generating random emails
import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

print (random_char(8)+"@gmail.com")

driver = webdriver.Chrome('/Users/IOKTWIEAETIQ/Downloads/chromedriver 3')

driver.get('https://www.thinbluelinetv.com/2021/07/minneapolis-likely-to-do-away-with-entire-police-department/')

selectRvote = driver.find_element_by_xpath('//*[@id="totalpoll-poll-51405"]/form/div[1]/div/div/div[2]/label[2]/div/div/div[2]/span')
selectRvote.click()

selectemailfield = driver.find_element_by_xpath('//*[@id="totalpoll-fields-email"]')
selectemailfield.send_keys(random_char(8)+'@gmail.com')

selectVotebutton = driver.find_element_by_xpath('//*[@id="totalpoll-poll-51405"]/form/div[4]/button[2]')
selectVotebutton.click()



driver.quit()

r = random.randint(7,15)

rtime = random.randint(0,5)

driver.quit()

time.sleep(.3)

for i in range(1):

    driver = webdriver.Chrome('/Users/IOKTWIEAETIQ/Downloads/chromedriver 3')

    driver.get('https://www.thinbluelinetv.com/2021/07/minneapolis-likely-to-do-away-with-entire-police-department/')

    selectRvote = driver.find_element_by_xpath('//*[@id="totalpoll-poll-51405"]/form/div[1]/div/div/div[2]/label[2]/div/div/div[2]/span')
    selectRvote.click()
    time.sleep(rtime)

    selectemailfield = driver.find_element_by_xpath('//*[@id="totalpoll-fields-email"]')
    selectemailfield.send_keys(random_char(r)+'@gmail.com')
    time.sleep(rtime)

    selectVotebutton = driver.find_element_by_xpath('//*[@id="totalpoll-poll-51405"]/form/div[4]/button[2]')
    selectVotebutton.click()
    time.sleep(3)

    driver.quit()