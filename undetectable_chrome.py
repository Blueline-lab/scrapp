#Scrap engine

import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()

options.headless=True
options.add_argument('--headless')



# setting profile
#options.user_data_dir = ""

# another way to set profile is the below (which takes precedence if both variants are used
#options.add_argument('--user-data-dir=~/Bureau/Scrapper')

# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    driver.get('https://monreseaumobile.arcep.fr/')
    element = driver.find_element(by=By.CLASS_NAME, value="mapboxgl-ctrl-geocoder--input")
    driver.save_screenshot("test.png")
