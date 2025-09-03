## Data from: 
## https://public.tableau.com/app/profile/victoria6405/viz/WalesHCAISurveillanceMonthlyDashboard/HBMonthlyDashboard

import time, csv
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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


print("Finding the Excel download link...")
wait = WebDriverWait(driver, 20)
try:
    # iframe_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))

    ## Select the iframe containing the button Image 'Download data'
    iframe_element = wait.until(
        EC.presence_of_element_located((
            By.XPATH, 
            '//*[@id="embedded-viz-wrapper"]/iframe'))
            )
    print("iframe found")

    ## Switch Selenium's context to the iframe
    driver.switch_to.frame(iframe_element)

    ## Try to find the element inside the iframe
    image_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabZoneId861"]/div/div/div/a/img')))
    print("image button found!")
    image_button.click()
    time.sleep(2)
    print("Excel file downloaded!")


except TimeoutException:
    print("Iframe or button image not found.")


