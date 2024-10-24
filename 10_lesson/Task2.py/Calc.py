from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calc:
    """
    Этот класс представлет сущность -
    "Калькулятор", - страница, где работают функции калькулятора
    """
    def __init__(self, driver):
        self._driver = driver
        """Открывает страницу сайта в браузере Хром"""
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        """Делает окно браузера максимальным по размеру"""
        self._driver.maximize_window()

    def timer(self) -> None:
        """Устанавливает таймер, после введения валидных данных в поле"""
        click = self._driver.find_element(By.ID, "delay")
        ActionChains(self._driver)\
            .double_click(click)\
            .perform()
        time = self._driver.find_element(By.ID, "delay")
        time.send_keys("45")

    def nums(self) -> None:
        """Кликает на нужные кнопки, для вычислений"""
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result(self) -> int:
        """Вычисляет -> реализует процесс 'сложения' чисел и выдает результат"""
        WebDriverWait(self._driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="15"]')))
        res = self._driver.find_element(By.XPATH, '//div[text()="15"]').text
        return int(res)
