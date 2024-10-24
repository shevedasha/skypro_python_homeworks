from selenium.webdriver.common.by import By

class Cart:
    """
    Этот класс представлет сущность -
    "Страница с товарами", - тут представлены товары магазина
    """
    def __init__(self, driver):
        self._driver = driver

    def add_backpack(self) -> None:
        """Выбирает определнный товар"""
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_tshirt(self) -> None:
        """Выбирает определнный товар"""
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self) -> None:
        """Выбирает определнный товар"""
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def cart(self) -> None:
        """Переходит в корзину"""
        self._driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()

    def checkout(self) -> None:
        """Кликает на кнопку 'Checkout'"""
        self._driver.find_element(By.ID, "checkout").click()
