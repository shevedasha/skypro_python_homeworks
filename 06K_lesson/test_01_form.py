import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

element_1 = driver.find_element(By.CSS_SELECTOR, "input[name=first-name]")
element_1.send_keys("Иван")
element_2 = driver.find_element(By.CSS_SELECTOR, "input[name=last-name]")
element_2.send_keys("Петров")
element_3 = driver.find_element(By.CSS_SELECTOR, "input[name=address]")
element_3.send_keys("Ленина, 55-3")
element_4 = driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]")
element_4.send_keys()
element_5 = driver.find_element(By.CSS_SELECTOR, "input[name=city]")
element_5.send_keys("Москва")
element_6 = driver.find_element(By.CSS_SELECTOR, "input[name=country]")
element_6.send_keys("Россия")
element_7 = driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]")
element_7.send_keys("test@skypro.com")
element_8 = driver.find_element(By.CSS_SELECTOR, "input[name=phone]")
element_8.send_keys("+7985899998787")
element_9 = driver.find_element(By.CSS_SELECTOR, "input[name=job-position]")
element_9.send_keys("QA")
element_10 = driver.find_element(By.CSS_SELECTOR, "input[name=company]")
element_10.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button").click()

element_4_color = driver.find_element(By.ID, "zip-code").value_of_css_property("color")
element_1_color = driver.find_element(By.ID, "first-name").value_of_css_property("color")
element_2_color = driver.find_element(By.ID, "last-name").value_of_css_property("color")
element_3_color = driver.find_element(By.ID, "address").value_of_css_property("color")
element_5_color = driver.find_element(By.ID, "city").value_of_css_property("color")
element_6_color = driver.find_element(By.ID, "country").value_of_css_property("color")
element_7_color = driver.find_element(By.ID, "e-mail").value_of_css_property("color")
element_8_color = driver.find_element(By.ID, "phone").value_of_css_property("color")
element_9_color = driver.find_element(By.ID, "job-position").value_of_css_property("color")
element_10_color = driver.find_element(By.ID, "company").value_of_css_property("color")


def test_1():
    color = element_4_color
    assert color == "rgba(132, 32, 41, 1)"


def test_2():
    color = element_1_color and element_2_color and element_3_color and element_5_color and element_6_color and element_7_color and element_8_color and element_9_color and element_10_color
    assert color == "rgba(15, 81, 50, 1)"


driver.quit()
