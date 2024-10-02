from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
    new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(new_button)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
