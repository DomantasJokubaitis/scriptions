from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://inventwithpython.com")

email_elem = driver.find_element(By.ID, "mce-EMAIL")
email_elem.send_keys("some.mail@gmail.com")
subscribe_button = driver.find_element(By.ID, "mc-embedded-subscribe")
subscribe_button.click()

driver.quit()
