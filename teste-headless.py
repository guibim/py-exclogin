from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configurações para rodar o Chrome em modo headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa o Chrome sem interface gráfica
options.add_argument('--window-size=1920,1080')  # Define o tamanho da janela


# Inicia o driver do Chrome com as opções headless
driver = webdriver.Chrome(options=options)

try:
    # Teste 1 - Login com credenciais inválidas
    driver.get("https://the-internet.herokuapp.com/login")

    # Encontra os campos de login e senha
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

    # Preenche os campos com dados inválidos e clica no botão de login
    username.send_keys("usuarioteste")
    password.send_keys("senhateste")
    login_button.click()

    # Espera a mensagem de erro aparecer
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        print("Teste 1 - Erro: Credenciais inválidas", error_message.text)
    except TimeoutException:
        print("Teste 1 - Mensagem de erro não apareceu")

    # Tempo para observar o resultado
    time.sleep(3)

    # Teste 2 - Login com credenciais válidas

    # Recarrega a página para iniciar o segundo teste
    driver.get("https://the-internet.herokuapp.com/login")

    # Encontra os campos de login e senha
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")

    # Preenche os campos com dados válidos e clica no botão de login
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button.click()

    # Espera a mensagem de sucesso aparecer
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        print("Teste 2 - Sucesso no Login", success_message.text)
    except TimeoutException:
        print("Teste 2 - Mensagem de sucesso não apareceu")

    # Logout após o login bem sucedido
    try:
        # Espera até o botão de logout estar presente e então clica nele
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
        )
        logout_button.click()
        print("Logout realizado com sucesso.")
    except TimeoutException:
        print("Botão de logout não apareceu.")

    # Tempo para observar o resultado
    time.sleep(3)


finally:
    driver.quit()
