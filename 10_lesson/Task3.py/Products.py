from selenium.webdriver.common.by import By

class Products:
    """
    Этот класс представлет собой страцицу -
    с полями для ввода личных данных клиента
    """
    def __init__(self, driver):
        self._driver = driver

    def first_name(self, first: str) -> None:
        """Поле для ввода имени"""
        self._driver.find_element(By.ID, "first-name").send_keys(first)

    def last_name(self, last: str) -> None:
        """Поле для ввода фамилии"""
        self._driver.find_element(By.ID, "last-name").send_keys(last)

    def post_code(self, post: str) -> None:
        """Поле для ввода индекса"""
        self._driver.find_element(By.ID, "postal-code").send_keys(post)

    def confirm(self) -> None:
        """Кнопка для сохранения данных"""
        self._driver.find_element(By.ID, "continue").click()
