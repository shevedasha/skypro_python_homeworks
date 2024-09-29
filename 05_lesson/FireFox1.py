from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)

close = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")))
close.click()
sleep(5)
