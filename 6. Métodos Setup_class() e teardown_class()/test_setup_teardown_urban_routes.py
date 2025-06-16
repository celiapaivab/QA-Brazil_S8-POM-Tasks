from selenium import webdriver
import time
from urban_routes_main_page import UrbanRoutesPage

# Crie uma classe para ambos os testes
class TestUrbanRoutes:

    # Inicialize o driver do Chrome uma vez para a classe
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_personal_bike_option(self):
        self.driver.get('https://cnt-404ba860-ed15-4107-a334-a76bd19f5e81.containerhub.tripleten-services.com?lng=pt')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        urban_routes_page.click_personal_option()
        time.sleep(2)
        urban_routes_page.click_bike_icon()
        time.sleep(2)
        actual_value = urban_routes_page.get_bike_text()
        expected_value = "Bicicleta"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    def test_duration_personal_bike_option(self):
        self.driver.get('https://cnt-404ba860-ed15-4107-a334-a76bd19f5e81.containerhub.tripleten-services.com?lng=pt')
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')
        urban_routes_page.click_personal_option()
        time.sleep(2)
        urban_routes_page.click_bike_icon()
        time.sleep(2)
        actual_duration = urban_routes_page.get_duration_text()
        expected_duration = "Duração"
        assert expected_duration in actual_duration, f"Esperado '{expected_duration}', mas obtido '{actual_duration}'"

    # Feche o navegador depois que todos os testes forem feitos
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()