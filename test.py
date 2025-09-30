from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open your Cloudflare-protected page
driver.get("https://servicos.pf.gov.br/epol-sinic-publico/")

# Wait a few seconds for Cloudflare challenge to complete
time.sleep(10)  # adjust depending on challenge timing

iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))  # adjust selector if needed
)
driver.switch_to.frame(iframe)

checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
)
checkbox.click()

time.sleep(10)
driver.quit()