from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- Setup Headless Chrome ---
# Create an instance of ChromeOptions
chrome_options = Options()

# Add the headless argument
# This tells Chrome to run without a user interface
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080") # Optional: Specify window size

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# --- Open the Website ---
# url = "https://automationintesting.com/selenium/testpage/"
url = "https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard"

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

finally:
    # --- Close the Driver ---
    # It's important to quit the driver to close the browser instance
    # and free up system resources.
    if driver:
        driver.quit()
        print("Browser closed.")