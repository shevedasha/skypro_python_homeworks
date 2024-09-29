from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(
   "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary')]")
button.click()
sleep(5)
