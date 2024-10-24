from selenium.webdriver.common.by import By

class Products:

    def __init__(self, driver):
        self._driver = driver

    def first_name(self, first: str) -> None:
        self._driver.find_element(By.ID, "first-name").send_keys(first)

    def last_name(self, last: str) -> None:
        self._driver.find_element(By.ID, "last-name").send_keys(last)

    def post_code(self, post: str) -> None:
        self._driver.find_element(By.ID, "postal-code").send_keys(post)

    def confirm(self) -> None:
        self._driver.find_element(By.ID, "continue").click()
    