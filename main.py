from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# --- Setup Headless Chrome ---
# Create an instance of ChromeOptions
chrome_options = Options()

# Add the headless argument
# This tells Chrome to run without a user interface
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080") # Optional: Specify window size

# Add user agent and other arguments
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# --- Open the Website ---
# url = "https://automationintesting.com/selenium/testpage/"
url = "https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard"
url = "https://www2.nphs.wales.nhs.uk/WHAIPDocs.nsf"
try:
    print(f"Opening {url} in headless mode...")
    driver.get(url)
    
    # Verify by printing the page title
    print(f"Page title: '{driver.title}'")
    print("Successfully opened the page.")

    # Print all HTML code from the page
    print("\n--- HTML Source Code ---")
    print(driver.page_source)
    print("------------------------")



except Exception as e:
    print(f"An error occurred: {e}")

