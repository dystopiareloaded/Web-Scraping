import time
#import chromedriver_autoinstaller
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDrivern
driver_path = r"C:\Users\Dell\OneDrive\Desktop\chromedriver.exe"  # <-- Change this to your new ChromeDriver path

# Set Chrome options to launch in Incognito Mode
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Open Chrome in Incognito Mode

# Initialize WebDriver with undetected_chromedriver and custom ChromeDriver path
driver = uc.Chrome(driver_executable_path=driver_path, options=chrome_options)

# Open Smartprix website
driver.get('https://www.smartprix.com/mobiles')

# Wait for page load
time.sleep(2)

# Click the first checkbox
driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)

# Click the second checkbox
driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:


# Click on the third element
    driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)

    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)
 

# Option to keep the browser open for debugging
input("Press Enter to close the browser...")

# Close browser
driver.quit()
