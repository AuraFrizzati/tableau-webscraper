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
time.sleep(1)
print("Rejecting cookies...")
btn_reject_cookies = driver.find_element(by="id", value = "onetrust-reject-all-handler")
btn_reject_cookies.click()
time.sleep(1)

#download_data_button.click()
#download_data_button = driver.find_element(by="class name", value =  "tab-image tab-widget")

# Find the link to the Excel file
# https://selenium-python.readthedocs.io/locating-elements.html
print("Finding the Excel download link...")

#/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[30]/div/div/div/a/img
# //*[@id="tabZoneId861"]/div/div/div/a/img
#Id861
# /html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[30]/div/div/div/a/img
# download_link_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="tabZoneId861"]/div/div/div/a'))
# )
# download_link_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//div[@id="tabZoneId861"]'))
# )

# <div class="tab-zone tab-widget tabSuppressVizTooltipsAndOverlays tabZone-bitmap" 
# id="tabZoneId861" style="z-index: 62; width: 138px; height: 28px; top: 659px; left: 858px;">
# <div class="tab-zone-margin" style="inset: 0px; position: absolute; background-color: rgba(0, 0, 0, 0); border-width: 0px; border-style: none; border-color: rgb(0, 0, 0);"><div class="tab-zone-padding" style="inset: 0px; position: absolute;"><div class="tab-image tab-widget" style="position: absolute; overflow: hidden; inset: 0px;"><a href="https://www2.nphs.wales.nhs.uk/WHAIPDocs.nsf/3dc04669c9e1eaa880257062003b246b/d60242dff347082b80258a230046df01/$FILE/HCAI%20HB%20Dashboard%20Data.xlsx" target="_blank" style="position: absolute;"><img alt="Image" data-datasrc=

# image_element = driver.find_element(By.XPATH, "//*[@id='tabZoneId861']/div")
image_element = driver.find_element(By.XPATH, "//div[contains(@id,'tabZoneId861')]")
# ul = driver.find_element_by_xpath("//ul[contains(@class,'jobs-search__results')]")

# 2. Click the image element
image_element.click()

# Get the URL from the href attribute
#download_url = download_link_element.get_attribute('href')
print(f"Found download URL: {download_url}")


#download_link_element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "HCAI%20HWB%20Dashboard%20Data.xlsx")]'))
#)
# clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")
# btn_downlaod = driver.find_element(By.CLASS_NAME, value = "tab-image tab-widget")
#btn_downlaod = driver.find_element(By.XPATH, value = "//div[@id='tab-dashboard-region']")
#download_link_element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, '//div[@class="tab-image tab-widget"]/a[contains(@href, ".xlsx")]'))
#)
# Get the URL from the href attribute
#download_url = download_link_element.get_attribute('href')
#print(f"Found download URL: {download_url}")

# Close the browser session 
driver.quit()


