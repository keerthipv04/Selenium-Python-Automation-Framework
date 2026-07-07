import pytest
from selenium import webdriver


@pytest.fixture

def setup():
    print("Lauch browser")
    driver= webdriver.Chrome()
    driver.get("https://demoqa.com/login")
    driver.maximize_window()

    yield driver

    print("Close browser")
    driver.quit()