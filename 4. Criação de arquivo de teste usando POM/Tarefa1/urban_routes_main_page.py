from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Bicicleta")]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FROM_LOCATOR)
        )
        element.clear()
        element.send_keys(from_text)

    def enter_to_location(self, to_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TO_LOCATOR)
        )
        element.clear()
        element.send_keys(to_text)

    def click_personal_option(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PERSONAL_OPTION_LOCATOR)
        )
        element.click()

    def click_bike_icon(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BIKE_ICON_LOCATOR)
        )
        element.click()

    def get_bike_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BIKE_TEXT_LOCATOR)
        )
        return element.text
