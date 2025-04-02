import time
#import chromedriver_autoinstaller 
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Specify the path to your ChromeDriver
driver_path = r"C:\Users\Dell\OneDrive\Desktop\chromedriver.exe" # <-- Change this to your ChromeDriver path


# Set Chrome options to launch in Incognito Mode
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Open Chrome in Incognito Mode

# Initialize WebDriver with undetected_chromedriver and custom ChromeDriver path
driver = uc.Chrome(driver_executable_path=driver_path, options=chrome_options)

# Open smartprix website

website = 'https://www.smartprix.com/laptops'
driver.get(website)

time.sleep(2)

# Availability - out of stock

exclude_out_of_stock = driver.find_element(By.XPATH, value= '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
exclude_out_of_stock.click()

time.sleep(1)

# Availability - upcoming

exclude_upcoming = driver.find_element(By.XPATH, value= '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
exclude_upcoming.click()

time.sleep(1)
old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    Load_More = driver.find_element(By.XPATH, value= '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()

    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)
    
    if new_height == old_height:
        break
    old_height = new_height



html = driver.page_source

with open('smartprix-laptop.html', 'w', encoding='utf-8') as f:
    f.write(html)
 #Option to keep the browser open for debugging
input("Press Enter to close the browser...")

# Close browser
driver.quit()