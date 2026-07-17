import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup():
    print("Lauch browser")

    options = Options()

    # Run headless only when executed inside GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/login")
    driver.maximize_window()

    yield driver

    print("Close browser")
    driver.quit()
