import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\Dell\OneDrive\Desktop\chromedriver.exe"

# Set Chrome to launch in incognito mode

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = uc.Chrome(driver_executable_path=driver_path,options=chrome_options)

# Opem ajio-backpacks website

website = "https://www.ajio.com/men-backpacks/c/830201001"

driver.get(website)





old_height = driver.execute_script('return document.body.scrollHeight')
counter = 1

while True:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    
    print(counter)
    counter += 1

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    
    old_height = new_height


html = driver.page_source

with open('ajio-bags.html','w',encoding='utf-8') as f:
    f.write(html)

input('Press Enter to close the browser....')
driver.quit()

