from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.elements_page import ElementPage
from pages.login_page import LoginPage
import time
from pages.forms_page import FormPage
from pages.interaction_page import Interactions
from pages.alertsandforms_page import AlertsFrame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_all(setup):
    driver= setup

#login to the page
    login = LoginPage(driver)
    login.username_field("keerthana")
    login.password_field("Keerthana@04")
    login.login_button()
    time.sleep(2)

#click elements abd fill text box details
    elements= ElementPage(driver)
    elements.click_element_section()
    time.sleep(2)
    elements.click_text_box()
    elements.fill_text_box("Keerthana","keerthana@gmail.com","abcd colony", "abcd_2 colony")
    time.sleep(2)
    driver.back()
    time.sleep(2)

    
# just perfrom click action
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elements.check_box)).click()
    elements.click_check_box()
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elements.radio_button)).click()
    elements.click_radio_button()
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elements.web_tables)).click()
    elements.click_web_tables()
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elements.buttons)).click()
    elements.click_buttons_section()
    driver.back()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(elements.links)).click()
    elements.click_links()
    driver.back()

    elements.click_element_section()
    time.sleep(2)

#refresh the page
    driver.refresh()

#click form section and perform practice form actions
    forms = FormPage(driver)
    forms.click_form_section()
    time.sleep(2)

    forms.fill_practice_form(
        "Keerthana",
        "keerthi",
        "keerthi@gmail.com",
        "1234567890",
        "abcd colony",
        "Rajasthan",
        "Jaipur"
    )
   
    time.sleep(2)
    
    print("Form filled successfully")
    #forms.close_popup() #close button is not working properly so i have used refresh and back to the page
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    forms.click_form_section()  #clsoe the forms section
    time.sleep(5)

 #click alerts, frame and windows section and perform alert/window/frame actions
    alerts_frame = AlertsFrame(driver)
    alerts_frame.perform_alerts_frame_flow()
    time.sleep(2)

    driver.get("https://demoqa.com/interaction")
    time.sleep(2)
    

 #click form interaction and perform droppable(drag and drop) form actions 

    driver.get("https://demoqa.com/droppable")
    time.sleep(2)

    interaction = Interactions(driver)
    interaction.drag_and_drop()