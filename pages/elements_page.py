
from selenium.webdriver.common.by import By
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


#methods

    def click_element_section(self):
        self.driver.find_element(*self.element_section).click()
        

    def click_text_box(self):
        self.driver.find_element(*self.text_box).click()  

    def click_check_box(self):
        self.driver.find_element(*self.check_box).click()

    def click_radio_button(self):
        self.driver.find_element(*self.radio_button).click()

    def click_web_tables(self):
        self.driver.find_element(*self.web_tables).click()    

    def click_buttons_section(self):
        self.driver.find_element(*self.buttons).click()   

    def click_links(self):
        self.driver.find_element(*self.links).click()

    def click_broken_links(self):
        self.driver.find_element(*self.broken_links).click()    

    def click_upload_and_download(self):
        self.driver.find_element(*self.upload_download).click() 

    def click_dynamic_properties(self):
        self.driver.find_element(*self.dynamic_properties).click()  



    def fill_text_box(self, name, email, address, p_address):
        self.driver.find_element(*self.full_name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.curent_address).send_keys(address)
        self.driver.find_element(*self.permanent_address).send_keys(p_address)
        submit = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", submit)


    
