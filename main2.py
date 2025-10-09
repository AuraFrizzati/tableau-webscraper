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

# --- Configure download path ---
# Define the subfolder and create it if it doesn't exist
download_path = os.path.join(os.getcwd(), "data")
os.makedirs(download_path, exist_ok=True)
prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)

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

url = "https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard"

driver.get(url)

# Print the HTML content of the page
# print("\n--- HTML Source Code ---")
# print(driver.page_source)
# print("--- End of HTML Source Code ---")


# Wait for the reject cookies button to be clickable and click it
# Wait for the reject cookies button to be clickable and click it
print("Looking for cookies banner...")
wait = WebDriverWait(driver, 10)

try:
    # Wait for the cookie banner to appear and be clickable
    btn_reject_cookies = wait.until(
        EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
    )
    print("Cookie banner found, rejecting cookies...")
    btn_reject_cookies.click()
    time.sleep(2)
    print("Cookies rejected successfully!")
except TimeoutException:
    print("Cookie banner not found or not needed - continuing...")

print("Finding the Excel download link...")
wait = WebDriverWait(driver, 20)
try:
    # --- 2. Switch to the iFrame ---
    print("Finding and switching to the iframe...")
    iframe_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="embedded-viz-wrapper"]/iframe')))
    driver.switch_to.frame(iframe_element)
    print("Switched to iframe.")

    ## Try to find the element inside the iframe
    image_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabZoneId861"]/div/div/div/a/img')))
    print("image button found!")
    image_button.click()
    time.sleep(30)
    print("Excel file downloaded!")
    
    driver.save_screenshot("debug_screenshot.png")
    print("Screenshot 'debug_screenshot.png' saved.")

except TimeoutException as e:
    print(f"An element was not found in time: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


finally:
    # --- 6. Verify the download ---
    print(f"Checking for downloaded files in: {download_path}")
    try:
        files_in_data_folder = os.listdir(download_path)
        if files_in_data_folder:
            print(f"SUCCESS: File(s) found: {files_in_data_folder}")
        else:
            print("FAILURE: No files were downloaded to the 'data' directory.")
    except Exception as e:
        print(f"Could not check directory contents: {e}")
    
    driver.quit()
    print("Browser closed.")