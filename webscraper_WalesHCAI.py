## Data from: 
## https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard

import time, csv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard"

## Launch a browser using Selenium
driver = Chrome()
driver.get(url)


# Wait for the reject cookies button to be clickable and click it
time.sleep(3)
print("Rejecting cookies...")
btn_reject_cookies = driver.find_element(by="id", value = "onetrust-reject-all-handler")
btn_reject_cookies.click()
time.sleep(3)

#download_data_button.click()
#download_data_button = driver.find_element(by="class name", value =  "tab-image tab-widget")

# Find the link to the Excel file
# https://selenium-python.readthedocs.io/locating-elements.html
print("Finding the Excel download link...")
#download_link_element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "HCAI%20HWB%20Dashboard%20Data.xlsx")]'))
#)
# clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")
# btn_downlaod = driver.find_element(By.CLASS_NAME, value = "tab-image tab-widget")
btn_downlaod = driver.find_element(By.XPATH, value = "//div[@id='tab-dashboard-region']")
#download_link_element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, '//div[@class="tab-image tab-widget"]/a[contains(@href, ".xlsx")]'))
#)
# Get the URL from the href attribute
#download_url = download_link_element.get_attribute('href')
#print(f"Found download URL: {download_url}")

# Close the browser session 
driver.quit()