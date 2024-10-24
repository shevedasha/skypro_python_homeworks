from selenium.webdriver.common.by import By
import allure

class Color:

    def __init__(self, driver):
        self._driver = driver

    @allure.step("Вызвать подсветку поля 'zip-code'")
    def zip_color(self) -> str:
        """Цвет поля Код"""
        color = self._driver.find_element(
            By.ID, "zip-code").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'first-name'")
    def first_name_color(self) -> str:
        """Цвет поля Имя"""
        color = self._driver.find_element(
            By.ID, "first-name").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'last-name'")
    def last_name_color(self) -> str:
        """Цвет поля Фамилия"""
        color = self._driver.find_element(
            By.ID, "last-name").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'address'")
    def address_color(self) -> str:
        """Цвет поля Адрес"""
        color = self._driver.find_element(
            By.ID, "address").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'city'")
    def city_color(self) -> str:
        """Цвет поля Город"""
        color = self._driver.find_element(
            By.ID, "city").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'country'")
    def country_color(self) -> str:
        """Цвет поля Страна"""
        color = self._driver.find_element(
            By.ID, "country").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'e-mail'")
    def email_color(self) -> str:
        """Цвет поля эл.почта"""
        color = self._driver.find_element(
            By.ID, "e-mail").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'phone'")
    def number_color(self) -> str:
        """Цвет поля Телефон"""
        color = self._driver.find_element(
            By.ID, "phone").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'job-position'")
    def job_color(self) -> str:
        """Цвет поля Должность"""
        color = self._driver.find_element(
            By.ID, "job-position").value_of_css_property("color")
        return color
    
    @allure.step("Вызвать подсветку поля 'company'")
    def company_color(self) -> str:
        """Цвет поля Компания"""
        color = self._driver.find_element(
            By.ID, "company").value_of_css_property("color")
        return color
