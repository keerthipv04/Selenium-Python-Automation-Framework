from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AlertsFrame:

    def __init__(self, driver):
        self.driver = driver

        # Left Menu
        self.click_alert_section = (By.XPATH, "//div[text()='Alerts, Frame & Windows']")
        self.click_alerts = (By.XPATH, "//span[text()='Alerts']")

        # Alert
        self.simple_alert = (By.ID, "alertButton")

    def safe_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def open_alert_section(self):
        self.safe_click(self.click_alert_section)

    def open_alerts(self):
        self.safe_click(self.click_alerts)

    def simple_alert_popup(self):
        self.safe_click(self.simple_alert)
        WebDriverWait(self.driver,10).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def perform_alerts_frame_flow(self):

        # Open Alerts, Frame & Windows section
        self.open_alert_section()
        time.sleep(1)

        # Alerts
        self.open_alerts()
        time.sleep(1)

        self.simple_alert_popup()
        time.sleep(2)

        # Frames
        self.driver.get("https://demoqa.com/frames")
        time.sleep(2)

        # Nested Frames
        self.driver.get("https://demoqa.com/nestedframes")
        time.sleep(2)

        # Modal Dialogs
        self.driver.get("https://demoqa.com/modal-dialogs")
        time.sleep(2)
