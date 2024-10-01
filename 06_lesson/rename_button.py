from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    MyBatton = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
    BlueButton = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
    NewButton = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(NewButton)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
