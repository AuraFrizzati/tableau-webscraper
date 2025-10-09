from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

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
# Use different URLs based on environment
if os.environ.get('GITHUB_ACTIONS'):
    # Use a test URL that works on GitHub Actions
    url = "https://httpbin.org/get"
    print("Running on GitHub Actions - using test URL")
else:
    # Use the real URL when running locally
    url = "https://www2.nphs.wales.nhs.uk/WHAIPDocs.nsf"
    print("Running locally - using real URL")

try:
    print(f"Opening {url} in headless mode...")
    driver.get(url)
    
    # Verify by printing the page title
    print(f"Page title: '{driver.title}'")
    
    # Check if we got an error page instead of the real site
    if "This site can't be reached" in driver.page_source or "ERR_" in driver.page_source:
        print("ERROR: Cannot reach the website")
        print("This is likely due to network restrictions or geographic blocking")
    else:
        print("Website loaded successfully")
        
        # Only print HTML for test sites to avoid huge outputs
        if "httpbin" in url:
            print("\n--- HTML Source Code ---")
            print(driver.page_source[:1000])  # First 1000 chars only

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")

