from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.3)

try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_1 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text
    print(text_1)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
