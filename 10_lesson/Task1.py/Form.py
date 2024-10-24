from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.severity("Blocker")
@allure.feature("User form")
class Form:
    """
    Этот класс представлет сущность -
    "форма", которая нужна для заполения данных пользователем
    """

    def __init__(self, driver):
        self._driver = driver
        """Настраивает драйвер на неявное ожидание"""
        self._driver.implicitly_wait(10)
        """Открывает страницу сайта в браузере Хром"""
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        """Делает окно браузера максимальным по размеру"""
        self._driver.maximize_window()

    @allure.step("Заполнить поле валидными данными {first}")
    def first_name(self, first: str) -> None:
        """Поле для имени"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(first)

    @allure.step("Заполнить поле валидными данными {last}")
    def last_name(self, last: str) -> None:
        """Поле для фамилии"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(last)

    @allure.step("Заполнить поле валидными данными {address}") 
    def address(self, address: str) -> None:
        """Поле для адреса"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(address)

    @allure.step("Оставить поле пустым {zipcode}")
    def zip_code(self, zipcode: str) -> None:
        """Поле для кода"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(zipcode)

    @allure.step("Заполнить поле валидными данными {city}")  
    def city(self, city: str) -> None:
        """Поле для города"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(city)

    @allure.step("Заполнить поле валидными данными {country}")   
    def country(self, country: str) -> None:
        """Поле для страны"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(country)

    @allure.step("Заполнить поле валидными данными {email}")   
    def email(self, email: str) -> None:
        """Поле для эл.почты"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)

    @allure.step("Заполнить поле валидными данными {phone}")   
    def phone(self, phone: str) -> None:
        """Поле для номера телефона"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    @allure.step("Заполнить поле валидными данными {job}")   
    def job_position(self, job: str) -> None:
        """Поле для должности"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(job)

    @allure.step("Заполнить поле валидными данными {company}")    
    def company(self, company: str) -> None:
        """Поле для компании"""
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(company)

    @allure.step("Кликнуть на кнопку 'Submit")
    def click_submit(self) -> None:
        """Кнопка 'Submit'"""
        self._driver.find_element(By.CSS_SELECTOR, ".btn").click()
    