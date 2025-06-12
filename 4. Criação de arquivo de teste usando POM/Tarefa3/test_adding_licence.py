import time
from selenium import webdriver

from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM


def test_add_driver_license_personal_camping_option():
    driver = webdriver.Chrome()
    # Abra o aplicativo e atualize a URL após iniciar o servidor
    driver.get('https://cnt-bc065543-7eaa-4f9c-98f2-bb54bd40ee9e.containerhub.tripleten-services.com/')

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 1: Insira o endereço "De"
    urban_routes_page.enter_from_location('East 2nd Street, 601')

    # Etapa 2: Insira o endereço "Para"
    urban_routes_page.enter_to_location('1300 1st St')

    # Etapa 3: Escolha "Personal"
    urban_routes_page.click_personal_option()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 4: Clique em "Carsharing"
    urban_routes_page.click_carsharing_icon()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 5: Clique em "Reservar"
    urban_routes_page.click_book_button()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 6: Escolha "Camping"
    urban_routes_page.click_camping()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 7: Clique em “Adicionar uma carteira de motorista”
    urban_routes_page.click_add_driver_license()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 8: Preencha o campo “Nome”
    urban_routes_page.enter_first_name('Ana')
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 9: Preencha o campo “Sobrenome”
    urban_routes_page.enter_last_name('Silva')
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 10: Preencha o campo “Data de nascimento”
    urban_routes_page.enter_date_of_birth('24.04.1889')
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 11: Preencha o campo “Número”
    urban_routes_page.enter_number('01 01 123456')
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 12: Clique em "título" para tornar clicável o botão Adicionar
    urban_routes_page.click_title()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 13: Clique em “Adicionar”
    urban_routes_page.click_add_button()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 14: Verifique se a licença foi adicionada
    actual_value = urban_routes_page.get_verification_text()
    expected_value = "Obrigado! Os documentos foram enviados para verificação. Voltaremos com os resultados em breve"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"

    driver.quit()


