from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(
    "xpath", '//button[text()="Button with Dynamic ID"]').click()
sleep(5)
