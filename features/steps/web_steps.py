# features/steps/web_steps.py

from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

@when('I click the "{button_text}" button')
def step_click_button(context, button_text):
    """
    Step definition for clicking a button identified by its text.
    """
    try:
        # Find the button by its text and click it
        button = driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
        button.click()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Ensure that you close the browser after tests are done
def after_all(context):
    driver.quit()
