from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.total_price = (By.ID, 'total_price')
        self.delete_btn = (By.CLASS_NAME, 'cart_quantity_delete')
        self.alert = (By.CLASS_NAME, 'alert-warning')

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text

    def remove_product(self):
        self.driver.find_element(*self.delete_btn).click()

    def is_cart_empty(self):
        return self.driver.find_element(*self.alert).is_displayed()
