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
url = 'https://www.booking.com/searchresults.html?ss=Kolkata&ssne=Kolkata&ssne_untouched=Kolkata&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4As-HrsAGwAIB0gIkZDViMTg5ODItNDRkMS00ZTAxLWIxYWUtNTFkYTJkMDgzZTky2AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2092511&dest_type=city&checkin=2025-04-25&checkout=2025-04-26&group_adults=2&no_rooms=1&group_children=0'
driver.get(url)
time.sleep(5)



# Scroll until no more content is loaded
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Scrolled from {last_height} to {new_height}")

    if new_height == last_height:
        print("Reached end of page.")
        break
    last_height = new_height

# Save page source
html = driver.page_source
with open("bookinghotels.html", "w", encoding="utf-8") as f:
    f.write(html)

input("Press Enter to close the browser...")
driver.quit()
