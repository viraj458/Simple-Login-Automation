from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


username = "virajmalaka458@gmail.com"
password = "abc"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://github.com/login")


usernamefield = driver.find_element("id", "login_field")
usernamefield.send_keys(username)


passwordfield = driver.find_element("id", "password")
passwordfield.send_keys(password)


driver.find_element("name", "commit").click()
