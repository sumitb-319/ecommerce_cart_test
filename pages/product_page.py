from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product = (By.CSS_SELECTOR, '.product-container')
        self.add_to_cart_btn = (By.CSS_SELECTOR, '.ajax_add_to_cart_button')
        self.cart_popup = (By.ID, 'layer_cart')
        self.proceed_btn = (By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')

    def add_first_product_to_cart(self):
        product = self.driver.find_element(*self.first_product)
        ActionChains(self.driver).move_to_element(product).perform()
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.proceed_btn).click()
