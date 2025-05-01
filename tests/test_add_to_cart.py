from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    HomePage(driver).go_to_women_section()
    ProductPage(driver).add_first_product_to_cart()
    ProductPage(driver).go_to_cart()
    price = CartPage(driver).get_total_price()
    assert price.startswith('$'), "Price not displayed correctly"
