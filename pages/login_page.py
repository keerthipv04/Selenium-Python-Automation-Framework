from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "userName")
        self.password_locator = (By.ID, "password")
        self.login_locator = (By.ID, "login")
        self.error_locator = (By.ID, "name")
        self.logout_locator = (By.ID, "submit")

    def username_field(self, username):
        username_box = self.driver.find_element(*self.username_locator)
        username_box.clear()
        username_box.send_keys(username)

    def password_field(self, password):
        password_box = self.driver.find_element(*self.password_locator)
        password_box.clear()
        password_box.send_keys(password)

    def login_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)

    def error_msg(self):
        error = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.error_locator)
        )
        return error.text

    def logout_btn(self):
    button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.logout_locator)
    )
    self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
    self.driver.execute_script("arguments[0].click();", button)
