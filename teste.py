from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Especifique o caminho para o arquivo de preferências do perfil do Edge
profile_path = "C:\\Users\\dhona\\AppData\\Local\\Microsoft\\Edge\\User Data"

edge_options = webdriver.EdgeOptions()
edge_options.add_argument(f"user-data-dir={profile_path}")
edge_options.add_argument("start-maximized")  # Abrir o navegador maximizado

try:
    driver = webdriver.Edge(options=edge_options)

    driver.get('https://bing.com')

    element = driver.find_element(By.ID, 'sb_form_q')
    element.send_keys('WebDriver')
    element.submit()

    # ... (continuar com o restante do seu código)

    # Não use driver.quit() aqui, para manter a sessão normal aberta
    # O navegador continuará aberto e você poderá interagir manualmente com ele

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Para manter o navegador aberto e poder interagir manualmente, aguarde indefinidamente.
while True:
    time.sleep(10)  # Intervalo de espera de 10 segundos (você pode ajustar conforme necessário)
