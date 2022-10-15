from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.freecodecamp.org/")
driver.maximize_window()

sss = driver.find_element(By.CLASS_NAME,"navatar")
sss.click()

aaa = driver.find_element(By.ID, "email")
aaa.send_keys("virajmalaka458@gmail.com")

