from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for A in range(5):
    button_add = driver.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(5)
    buttons_delete = driver.find_elements("xpath", '//button[text()="Delete"]')

print(
    f"Выводим размер списка: {len(buttons_delete)}")
