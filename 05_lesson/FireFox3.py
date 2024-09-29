from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
sleep(3)
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
sleep(3)
password.send_keys("SuperSecretPassword!")

login = driver.find_element(By.TAG_NAME, "button").click()
sleep(3)
