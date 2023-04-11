import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.saucedema.com/'
driver.get(url)
driver.maximize_window()

login_user = 'standard_user'
password_user = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[]@id='user-name']")
user_name.send_keys(login_user)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_user)

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()


# this script helps to scroll page horizontal and vertical according to set coordinates in pixels
# driver.execute_script('window.scrollTo(0, 500)')

# this action will help to move to element on a page
action = ActionChains(driver)
red_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(red_shirt).perform()


# how to take a screenshot and save it in a directory with file name as a time it created
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_date + ' .png'
driver.save_screenshot('C:....path to folder ' + name_screenshot)