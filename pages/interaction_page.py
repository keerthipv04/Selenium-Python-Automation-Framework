from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Interactions:

    def __init__(self, driver):
        self.driver = driver

        self.drag_element = (By.ID, "draggable")
        self.drop_element = (By.ID, "droppable")

    def drag_and_drop(self):
        source = self.driver.find_element(*self.drag_element)
        target = self.driver.find_element(*self.drop_element)

        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()