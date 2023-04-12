import datetime
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()

login_user = 'standard_user'
password_user = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_user)

"""clear method will clear data from field"""
#time.sleep(6)
#user_name.clear()

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_user)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

"""working with hidden menu - about button"""
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(3)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
time.sleep(3)

