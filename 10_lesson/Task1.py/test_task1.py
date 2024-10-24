from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
from Form import Form
from Color import Color 

@allure.severity("Minor")
@allure.feature("Form")
@allure.title("Field color")
@allure.description("Вывод цвета поля в зависимости от валидности вводимых данных")
def test_task1():
    driver = webdriver.Chrome()

    form = Form(driver)

    form.first_name("Иван")
    form.last_name("Петров")
    form.address("Ленина, 55-3")
    form.zip_code("")
    form.city("Москва")
    form.country("Россия")
    form.email("test@skypro.com")
    form.phone("+7985899998787")
    form.job_position("QA")
    form.company("SkyPro")
    form.click_submit()

    color = Color(driver)

    first = color.first_name_color()
    last = color.last_name_color()
    address = color.address_color()
    zip_code = color.zip_color()
    city = color.city_color()
    country = color.country_color()
    email = color.email_color()
    phone = color.number_color()
    job = color.job_color()
    company = color.company_color()

    with allure.step("Проверить, что поле 'zip-code' подсвечено красным"):
        assert zip_code == "rgba(132, 32, 41, 1)"

    with allure.step("Проверить, что все остальные поля подсвечены зеленым"):
        color = [first, last, address, city, country, email, phone, job, company]
    for c in color:
        assert c == "rgba(15, 81, 50, 1)"
    """Закрывает браузер"""
    driver.quit()
