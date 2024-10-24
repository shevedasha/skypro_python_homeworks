from selenium.webdriver.common.by import By
import re

class Total:
    """
    Этот класс представлет сущность -
    "Total", - своего пода калькулятор для подсчета стоимости покупок
    """
    def __init__(self, driver):
        self._driver = driver

    def total_price(self) -> float:
        """Суммирует -> выдает итоговую сумму покупок"""
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        res = re.sub("[Total: $]", "", total)
        return float(res)
