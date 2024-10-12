from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Authorization import Auth
from Products import Products
from Yourcart  import Cart
from Total import Total

def test_task_3():
    driver = webdriver.Chrome()
    auth = Auth(driver)

    auth.login("standard_user")
    auth.password("secret_sauce")
    auth.confirm_auth()

    cart = Cart(driver)

    cart.add_backpack()
    cart.add_tshirt()
    cart.add_onesie()
    cart.cart()
    cart.checkout()

    prod = Products(driver)

    prod.first_name("Dasha")
    prod.last_name("Sheveleva")
    prod.post_code("620000")
    prod.confirm()

    sleep (20)

    total = Total(driver)
    price = total.total_price()

    assert price == 58.29

    driver.quit()
 