from selenium.webdriver.common.by import By

class Auth:
    """
    Этот класс представлет сущность -
    "Авторизация", - страница для авторизации в системе
    """
    def __init__(self, driver):
        self._driver = driver
        """Настраивает драйвер на неявное ожидание"""
        self._driver.implicitly_wait(10)
        """Открывает страницу сайта в браузере Хром"""
        self._driver.get("https://www.saucedemo.com/")
        """Делает окно браузера максимальным по размеру"""
        self._driver.maximize_window()

    def login(self, login: str) -> None:
        """Поле для ввода логина"""
        self._driver.find_element(By.ID, "user-name").send_keys(login)
      
    def password(self, password: str) -> None:
        """Поле для ввода пароля"""
        self._driver.find_element(By.ID, "password").send_keys(password)

    def confirm_auth(self) -> None:
        """Кнопка для сохранения логина/пароля"""
        self._driver.find_element(By.ID, "login-button").click()
