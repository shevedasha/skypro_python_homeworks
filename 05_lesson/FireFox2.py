from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.TAG_NAME, "input")
input.send_keys("1000")
sleep(3)
input.clear()
sleep(3)
input.send_keys("999")
sleep(3)
