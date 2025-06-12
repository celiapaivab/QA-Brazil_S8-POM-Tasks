from selenium.webdriver.common.by import By


# Definição da classe da página, dos localizadores e do método na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Bicicleta")]')

    def __init__(self, driver):
        self.driver = driver  # Inicializar o driver

    def enter_from_location(self, from_text):
        # Inserir De
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Inserir Para
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_personal_option(self):
        # Clicar Personal
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()

    def click_bike_icon(self):
        # Clicar no ícone Bicicleta
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        # Retornar o texto "Bicicleta"
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text
