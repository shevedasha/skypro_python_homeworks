from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.3)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
    attribute = driver.find_element(By.ID, "award").get_attribute("src")
    print(attribute)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
