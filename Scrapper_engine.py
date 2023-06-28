#Scrap engine


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = uc.ChromeOptions()
options.headless=True
#options.add_argument('--headless')

driver = uc.Chrome(options=options)



with driver:
    driver.get('https://map.snapchat.com/ttp/snap/W7_EDlXWTBiXAEEniNoMPwAAYeHRhaXhzeGl3AYjqT03tAYjqT00TAAAAAQ/@2.568200,-72.638095,17.00z')
    driver.implicitly_wait(10)

    driver.save_screenshot("1.png")
    
    
    #search = driver.find_element(By.NAME, 'Vous confirmez être âgé(e) de 16&nbsp;ans ou plus').click()
    
   
  
   
    
    driver.save_screenshot("cap.png")

