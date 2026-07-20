from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ElementPage():
    def __init__(self, driver):
        self.driver= driver
        #locators
        self.element_section= (By.XPATH,"//div[text()='Elements']")
        self.text_box= (By.XPATH,"//span[text()='Text Box']")
        self.check_box= (By.XPATH,"//span[text()='Check Box']")
        self.radio_button=(By.XPATH,"//span[text()='Radio Button']")
        self.web_tables=(By.XPATH,"//span[text()='Web Tables']")
        self.buttons=(By.XPATH,"//span[text()='Buttons']") 
        self.links=(By.XPATH,"//span[text()='Links']")
        self.broken_links=(By.XPATH,"//span[text()='Broken Links - Images']")
        self.upload_download=(By.XPATH,"//span[text()='Upload and Download']")
        self.dynamic_properties=(By.XPATH,"//span[text()='Dynamic Properties']")

        #text box section
        self.full_name=(By.ID,"userName")
        self.email=(By.ID,"userEmail")
        self.curent_address=(By.ID,"currentAddress")
        self.permanent_address= (By.ID,"permanentAddress")
        self.submit_button= (By.ID,"submit")


    #new reusable helper
    def safe_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)


#methods

    def click_element_section(self):
        self.safe_click(self.element_section)

    def click_text_box(self):
        self.safe_click(self.text_box)

    def click_check_box(self):
        self.safe_click(self.check_box)

    def click_radio_button(self):
        self.safe_click(self.radio_button)

    def click_web_tables(self):
        self.safe_click(self.web_tables)

    def click_buttons_section(self):
        self.safe_click(self.buttons)

    def click_links(self):
        self.safe_click(self.links)

    def click_broken_links(self):
        self.safe_click(self.broken_links)

    def click_upload_and_download(self):
        self.safe_click(self.upload_download)

    def click_dynamic_properties(self):
        self.safe_click(self.dynamic_properties)


    def fill_text_box(self, name, email, address, p_address):
        self.driver.find_element(*self.full_name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.curent_address).send_keys(address)
        self.driver.find_element(*self.permanent_address).send_keys(p_address)
        submit = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", submit)
