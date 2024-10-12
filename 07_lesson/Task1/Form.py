from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Form:

    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(10) 
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    def first_name(self, first):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(first)

    def last_name(self, last):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(last)
        
    def address(self, address):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(address)
        
    def zip_code(self, zipcode):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(zipcode)
        
    def city(self, city):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(city)
        
    def country(self, country):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(country)
        
    def email(self, email):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)
        
    def phone(self, phone):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(phone)
        
    def job_position(self, job):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(job)
        
    def company(self, company):
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(company)
        
    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, ".btn").click()
        
    







#         driver.implicitly_wait(10) 
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# element_1 = driver.find_element(By.CSS_SELECTOR, "input[name=first-name]")
# element_1.send_keys("Иван")
# element_2 = driver.find_element(By.CSS_SELECTOR, "input[name=last-name]")
# element_2.send_keys("Петров")
# element_3 = driver.find_element(By.CSS_SELECTOR, "input[name=address]")
# element_3.send_keys("Ленина, 55-3")
# element_4 = driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]")
# element_4.send_keys()
# element_5 = driver.find_element(By.CSS_SELECTOR, "input[name=city]")
# element_5.send_keys("Москва")
# element_6 = driver.find_element(By.CSS_SELECTOR, "input[name=country]")
# element_6.send_keys("Россия")
# element_7 = driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]")
# element_7.send_keys("test@skypro.com")
# element_8 = driver.find_element(By.CSS_SELECTOR, "input[name=phone]")
# element_8.send_keys("+7985899998787")
# element_9 = driver.find_element(By.CSS_SELECTOR, "input[name=job-position]")
# element_9.send_keys("QA")
# element_10 = driver.find_element(By.CSS_SELECTOR, "input[name=company]")
# element_10.send_keys("SkyPro")

# driver.find_element(By.CSS_SELECTOR, "button").click()

# element_4_color = driver.find_element(By.ID, "zip-code").value_of_css_property("color")
# element_1_color = driver.find_element(By.ID, "first-name").value_of_css_property("color")
# element_2_color = driver.find_element(By.ID, "last-name").value_of_css_property("color")
# element_3_color = driver.find_element(By.ID, "address").value_of_css_property("color")
# element_5_color = driver.find_element(By.ID, "city").value_of_css_property("color")
# element_6_color = driver.find_element(By.ID, "country").value_of_css_property("color")
# element_7_color = driver.find_element(By.ID, "e-mail").value_of_css_property("color")
# element_8_color = driver.find_element(By.ID, "phone").value_of_css_property("color")
# element_9_color = driver.find_element(By.ID, "job-position").value_of_css_property("color")
# element_10_color = driver.find_element(By.ID, "company").value_of_css_property("color")