import datetime
import pytest
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

"""authorization"""
login_user = 'standard_user'
password_user = 'secret_sauce'
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_user)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_user)
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

"""add Product #1 to cart"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
time.sleep(3)

"""cart info product #1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
assert value_cart_product_1 == value_product_1
cart_price_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = cart_price_product_1.text
assert value_cart_price_product_1 == value_price_product_1
