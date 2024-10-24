import pytest
from selenium import webdriver
from Calc import Calc
import allure

@allure.severity("Bloker")
@allure.feature("Addition")
@allure.title("Basic functions")
@allure.description("Проверка базовой функции калькулятора - сложения")
def test_task_2():

    driver = webdriver.Chrome()

    with allure.step("Открыть сайт в браузере"):
        calc = Calc(driver)

    with allure.step("Настроить таймер на 45 секунд"):
        calc.timer()

    with allure.step("Кликнуть на '7', '+' '8', '=' "):
        calc.nums()
        res = calc.result()

    with allure.step("Проверить, что результат верный"):
        assert res == 15
    """Закрывает браузер"""
    driver.quit()
