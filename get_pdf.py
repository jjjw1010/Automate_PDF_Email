from dotenv import load_dotenv
import os

# Load env variables 
load_dotenv()
PROJECT_PATH = os.getenv("PROJECT_PATH")
WEBSITE_URL = os.getenv("WEBSITE_URL")
ARMSTRONG_ID = os.getenv("ARMSTRONG_ID")
ARMSTRONG_PW = os.getenv("ARMSTRONG_PW")

###################################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pyautogui
from datetime import datetime

# Set custom download directory
download_path = os.path.abspath(PROJECT_PATH)

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")  # Enable incognito mode

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

###################################################################
# Open Armstrong login page
driver.get(WEBSITE_URL)
time.sleep(3) 

username = driver.find_element(By.NAME, "username") 
username.send_keys(ARMSTRONG_ID, Keys.RETURN)
time.sleep(3)

password = driver.find_element(By.NAME, "password")
password.send_keys(ARMSTRONG_PW, Keys.RETURN)
time.sleep(3)

###################################################################

skip_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Skip']")))
skip_button.click()

# Wait for the account dashboard to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "viewStatement")))

###################################################################

# Click the "View Statement" link
view_statement_link = driver.find_element(By.ID, "viewStatement")
view_statement_link.click()
time.sleep(5)

###################################################################
# Wait for the PDF to download
pyautogui.hotkey('ctrl', 's')
time.sleep(5)

# Extract the full month name
full_month_name = datetime.now().strftime("%B")


# Type the desired file path and name
pyautogui.write(full_month_name + "_Armstrong_Statement.pdf")
pyautogui.press('enter')
time.sleep(2)

# Close the browser after a delay
time.sleep(5)
driver.quit()

###################################################################