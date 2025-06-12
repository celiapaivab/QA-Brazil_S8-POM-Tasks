from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[@class="mode" and text()="Personal"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '//img[contains(@src, "drive")]/parent::*')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Reservar"]')
    CAMPING_LOCATOR = (By.XPATH, "//div[@class='tcard-icon' and img[@alt='Camping']]")
    AUDI_TEXT_LOCATOR = (By.CSS_SELECTOR, "div.drive-preview-title")

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver
        self.wait = WebDriverWait(driver, 10)

    def enter_from_location(self, from_text):
        # Inserir De
        from_input = self.wait.until(EC.element_to_be_clickable(self.FROM_LOCATOR))
        from_input.clear()
        from_input.send_keys(from_text)
        from_input.send_keys(Keys.RETURN)

    def enter_to_location(self, to_text):
        # Inserir Para
        to_input = self.wait.until(EC.element_to_be_clickable(self.TO_LOCATOR))
        to_input.clear()
        to_input.send_keys(to_text)
        to_input.send_keys(Keys.RETURN)

    def click_personal_option(self):
        # Clicar Personal
        self.wait.until(EC.element_to_be_clickable(self.PERSONAL_OPTION_LOCATOR)).click()

    def click_carsharing_icon(self):
        # Clique no ícone Carsharing
        self.wait.until(EC.element_to_be_clickable(self.CARSHARING_ICON_LOCATOR)).click()

    def click_book_button(self):
       # Clique no botão Reservar
       self.wait.until(EC.element_to_be_clickable(self.BOOK_BUTTON_LOCATOR)).click()

    def click_camping(self):
        # Clique em Camping
        self.wait.until(EC.element_to_be_clickable(self.CAMPING_LOCATOR)).click()

    def get_audi_text(self):
        # Retornar o texto "Audi"
        audi_element = self.wait.until(EC.visibility_of_element_located(self.AUDI_TEXT_LOCATOR))
        return audi_element.text
