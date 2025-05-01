from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time

def test_remove_product_from_cart(driver):
    HomePage(driver).go_to_women_section()
    ProductPage(driver).add_first_product_to_cart()
    ProductPage(driver).go_to_cart()
    CartPage(driver).remove_product()
    time.sleep(3)
    assert CartPage(driver).is_cart_empty(), "Cart is not empty after deletion"
