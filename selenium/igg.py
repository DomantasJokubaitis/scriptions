from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys
import pyautogui
import time
import random

game = sys.argv[1]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0" 
]

options = Options()
options.add_argument(f'user-agent={random.choice(user_agents)}')

browser = webdriver.Firefox(options=options)
browser.maximize_window()

browser.get("https://igg-games.com")
search_elem = browser.find_element(By.CLASS_NAME, "uk-search-input")

pyautogui.moveTo(1300, 460, duration=2)
time.sleep(random.uniform(2, 5))
pyautogui.moveTo(1320, 450, duration=2)
pyautogui.click()


time.sleep(random.uniform(2, 5))
search_elem.send_keys(game)
time.sleep(random.uniform(2, 5))
search_elem.send_keys(Keys.ENTER)
