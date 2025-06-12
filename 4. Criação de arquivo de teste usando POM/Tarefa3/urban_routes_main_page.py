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
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, "//div[@class='np-text' and contains(text(), 'Adicionar carteira de motorista')]")
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and contains(text(), "Adicionar")]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Adicionar carteira de motorista")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, "//div[contains(@class, 'head') and contains(text(), 'Obrigado')]")

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

    def click_add_driver_license(self):
        # Clicar em Adicionar carteira de motorista
        self.wait.until(EC.element_to_be_clickable(self.ADD_DRIVER_LICENSE_LOCATOR)).click()

    def enter_first_name(self, first_name):
        # Digitar Nome
        first_name_input = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_LOCATOR))
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        # Digitar Sobrenome
        last_name_input = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_LOCATOR))
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def enter_date_of_birth(self, date_of_birth):
        # Inserir Data de nascimento
        dob_input = self.wait.until(EC.visibility_of_element_located(self.DATE_OF_BIRTH_LOCATOR))
        dob_input.clear()
        dob_input.send_keys(date_of_birth)

    def enter_number(self, number):
        # Digitar Número
        number_input = self.wait.until(EC.visibility_of_element_located(self.NUMBER_LOCATOR))
        number_input.clear()
        number_input.send_keys(number)

    def click_title(self):
        # Clicar Adicionar um título de carteira de motorista
        self.wait.until(EC.element_to_be_clickable(self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR)).click()

    def click_add_button(self):
        # Clicar no botão Adicionar
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON_LOCATOR)).click()

    def get_verification_text(self):
        # Retornar o texto de verificação
        element = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'head') and contains(text(), 'Obrigado')]")
        ))
        return element.text