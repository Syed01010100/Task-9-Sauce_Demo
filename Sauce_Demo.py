from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class SauceDemoAutomation:
    def __init__(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def login(self):
        # Navigate to the login page
        self.driver.get("https://www.saucedemo.com/")

        # Log in with the provided credentials
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@name='login-button']")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Wait for the page to load
        time.sleep(2)

    def fetch_title(self):
        return self.driver.title

    def fetch_url(self):
        return self.driver.current_url

    def save_page_contents(self):
        page_contents = self.driver.page_source
        with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
            file.write(page_contents)

    def shutdown(self):
        self.driver.quit()
if __name__ == "__main__":
    demo = SauceDemoAutomation()
    demo.login()  # Log in for manual checks or execution
    print(f"Title of the page after login: {demo.fetch_title()}")
    print(f"Current URL of the page after login: {demo.fetch_url()}")
    demo.save_page_contents()  # Save page contents if needed
    demo.shutdown()  # Clean up