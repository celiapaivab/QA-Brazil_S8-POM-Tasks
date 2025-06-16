from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Bicicleta")]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duração")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FROM_LOCATOR)
        )
        element.clear()
        element.send_keys(from_text)

    def enter_to_location(self, to_text):
        # Inserir Para
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TO_LOCATOR)
        )
        element.clear()
        element.send_keys(to_text)

    def click_personal_option(self):
        # Clicar Personal
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PERSONAL_OPTION_LOCATOR)
        )
        element.click()

    def click_bike_icon(self):
        # Clicar no ícone Bicicleta
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BIKE_ICON_LOCATOR)
        )
        element.click()

    def get_bike_text(self):
        # Retornar o texto "Bicicleta"
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BIKE_TEXT_LOCATOR)
        )
        return element.text

    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    # Etapa para inserir os locais "De" e "Para"
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
