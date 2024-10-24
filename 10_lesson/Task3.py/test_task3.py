import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Authorization import Auth
from Products import Products
from Yourcart  import Cart
from Total import Total
import allure

@allure.severity("Bloker")
@allure.feature("Price calculation")
@allure.title("Total cost")
@allure.description("Проверка верности расчетов при оформлении заказа")
def test_task_3():
    driver = webdriver.Chrome()

    with allure.step("Открыть сайт в браузере"):
        auth = Auth(driver)

    with allure.step("Ввести валидные данные для авторизации"):
        with allure.step("Ввести валидный логин"):
            auth.login("standard_user")

        with allure.step("Ввести валидный пароль"):    
            auth.password("secret_sauce")

        with allure.step("Кликнуть на кнопку для авторизации"):        
            auth.confirm_auth()

    cart = Cart(driver)

    with allure.step("Выбрать необходимый товар"):
       cart.add_backpack()
       cart.add_tshirt()
       cart.add_onesie()
       cart.cart()
       with allure.step("Кликнуть на кнопку для перехода в следующий раздел"):
           cart.checkout()

    prod = Products(driver)

    with allure.step("Ввести валидные личные данные"):
        prod.first_name("Dasha")
        prod.last_name("Sheveleva")
        prod.post_code("620000")
        with allure.step("Кликнуть на кнопку для перехода к оплате"):
            prod.confirm()

    total = Total(driver)

    with allure.step("Выдать общую сумму покупок"):
        price = total.total_price()

    with allure.step("Проверить, что сумма покупок корректная"):
        assert price == 58.29
    
    """Закрывает браузер"""
    driver.quit()
