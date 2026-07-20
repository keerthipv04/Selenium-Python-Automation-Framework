import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage


def test_login(setup):

    driver = setup

    # Open the CSV file
    file = open("test_data/demoqa_file - Sheet1.csv","r")

    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Read each row
    for row in reader:

        username = row[0]
        password = row[1]

        driver.get("https://demoqa.com/login")

        login_page = LoginPage(driver)

        login_page.username_field(username)
        login_page.password_field(password)
        login_page.login_button()


        try:
            # Wait for logout button
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.ID, "submit"))
            )

            print("Login Successful :", username)

            # Logout
            login_page.logout_btn()

        except TimeoutException:

            print("Login Failed :", username)
            print(login_page.error_msg())

    file.close()
