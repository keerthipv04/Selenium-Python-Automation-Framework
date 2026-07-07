from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver= driver
        self.forms=(By.XPATH,"//div[text()='Forms']")
        self.click_practice_form= (By.XPATH,"//span[text()='Practice Form']")


# locators for practice form
        self.first_name=(By.ID,"firstName")
        self.last_name=(By.ID,"lastName")
        self.email_box=(By.ID,"userEmail")
        self.gender=(By.ID,"gender-radio-2")
        self.mobile_nmbr=(By.ID,"userNumber")
        self.current_address=(By.ID,"currentAddress")
        self.state_dropdown = (By.ID, "react-select-3-input")
        self.city_dropdown = (By.ID, "react-select-4-input")
        self.submit_btn=(By.ID,"submit")

    #methods

    def click_form_section(self):
        form = self.driver.find_element(*self.forms)
        self.driver.execute_script("arguments[0].click();", form)

        practice = self.driver.find_element(*self.click_practice_form)
        self.driver.execute_script("arguments[0].click();", practice)


    def fill_practice_form(self, f_name, l_name, email, number, address, state, city):
        self.driver.find_element(*self.first_name).send_keys(f_name)
        self.driver.find_element(*self.last_name).send_keys(l_name)
        self.driver.find_element(*self.email_box).send_keys(email)
        self.driver.find_element(*self.gender).click()
        self.driver.find_element(*self.mobile_nmbr).send_keys(number)
        self.driver.find_element(*self.current_address).send_keys(address)

        self.dropdown_state(state)
        self.dropdown_city(city)

        submit = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        self.driver.execute_script("arguments[0].click();", submit)

    def dropdown_state(self, state):
        state_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.state_dropdown))
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def dropdown_city(self, city):
        city_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.city_dropdown))
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)