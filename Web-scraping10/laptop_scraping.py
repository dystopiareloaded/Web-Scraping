import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Setup
driver_path = r"C:\Users\Dell\OneDrive\Desktop\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
driver = uc.Chrome(driver_executable_path=driver_path, options=chrome_options)

# Load URL
url = 'https://webscraper.io/test-sites/e-commerce/more/computers'
driver.get(url)

driver.find_element(By.XPATH, value='//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()

time.sleep(5)

# Scroll until no more content is loaded
#SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    driver.find_element(By.XPATH, value= '/html/body/div[1]/div[3]/div/div[2]/a').click()
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(last_height)
    print(new_height)    

    if new_height == last_height:
        print("Reached end of page.")
        break
    last_height = new_height

# Save page source
html = driver.page_source
with open("laptops.html", "w", encoding="utf-8") as f:
    f.write(html)

input("Press Enter to close the browser...")
driver.quit()
