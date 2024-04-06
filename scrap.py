from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import pandas as pd
import os

if os.path.exists('companies_info.csv'):
    companies_info = pd.read_csv('companies_info.csv')
else:
    companies_info = pd.DataFrame(columns=['name', 'number' , 'city'])



city = "indore"

def get_info():
    global companies_info , city
    names = driver.find_elements(By.CLASS_NAME, "qBF1Pd")
    numbers = driver.find_elements(By.CLASS_NAME, "UsdlK")

    # Iterate through each pair of name and number
    for name, number in zip(names, numbers):
        info = {
            'name': [name.text],
            'number': [number.text],
            'city': [city]
        }

        tmp = pd.DataFrame(info)
        print(tmp)
        companies_info = pd.concat([companies_info, tmp])
        # print(companies_info)

# Define the URL of the webpage you want to scrape
url = f"https://www.google.com/maps/search/consultancy+companies+in+{city}/"


# Set up the Selenium WebDriver
chrome_driver_path = r'C:\Users\Raj\Desktop\scrap\chromedriver-win64\chromedriver.exe'  # Path to your chromedriver executable
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
driver.get(url)
hover = ActionChains(driver)
iframe = driver.find_element(By.CLASS_NAME, "bJzME")
result_text = driver.find_element(By.CLASS_NAME, "IFMGgb")
result_text.click()

while len(driver.find_elements(By.CLASS_NAME, "HlvSq"))==0:
    ActionChains(driver)\
        .key_down(Keys.PAGE_DOWN)\
        .send_keys("abc")\
        .perform()


    time.sleep(0.5)



get_info()
companies_info.drop_duplicates(subset=['name','number'],inplace=True)
companies_info.to_csv('companies_info.csv',index=False)
# Add div around numbers






   






driver.quit()
