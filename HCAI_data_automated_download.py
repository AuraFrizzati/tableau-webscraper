import time, os
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# setup webdriver
# Define the subfolder and create it if it doesn't exist
download_path = os.path.join(os.getcwd(), "data")
os.makedirs(download_path, exist_ok=True)
chrome_options = Options()
prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)
driver = Chrome(options=chrome_options)

# open page https://www2.nphs.wales.nhs.uk/WHAIPDocs.nsf/
url = 'https://www2.nphs.wales.nhs.uk/WHAIPDocs.nsf/'
driver.get(url)

# [1] Access the iframe containing the link to the relevant data (HB HCAI dashboard data)
# //frame[@name='Right']
iframe_XPATH = "//frame[@name='Right']"

try:
    iframe_element = driver.find_element(By.XPATH, iframe_XPATH)
    print('Success: iFrame located!')
    ## Switch Selenium's context to the iframe
    driver.switch_to.frame(iframe_element)
    time.sleep(3)

except Exception as e:
    # FAILURE CHECK: Handle the case where the element wasn't found
    print(f"Error: iFrame not found! Details: {e}")

# [2] Identify the link to the dataset page
# <a href="/WHAIPDocs.nsf/61c1e930f9121fd080256f2a004937ed/d60242dff347082b80258a230046df01?OpenDocument" style="" 
# xpath="1"><acronym title="HB HCAI dashboard data">HB HCAI dashboard data</acronym></a>
try:
    HCAI_link_XPATH = "//a[acronym/@title='HB HCAI dashboard data']"
    HCAI_link_element = driver.find_element(By.XPATH, HCAI_link_XPATH)
    print(f"Link to dataset '{HCAI_link_element.text}' identified")
    HCAI_link_element.click()
    time.sleep(5)
    
except Exception as e:
    # FAILURE CHECK: Handle the case where the element wasn't found
    print(f"Error: dataset link not found! Details: {e}")

# [3] Extract the Publication date
try:
    date_pub_XPATH = "//font[contains(text(), 'Published')]/following-sibling::font[1]"
    date_pub_element = driver.find_element(By.XPATH, date_pub_XPATH)
    print(f"Link to dataset '{date_pub_element.text}' identified")
except Exception as e:
    # FAILURE CHECK: Handle the case where the element wasn't found
    print(f"Error: date of publication not found! Details: {e}")
    
# [4] Download the dataset
# <a href="/WHAIPDocs.nsf/61c1e930f9121fd080256f2a004937ed/d60242dff347082b80258a230046df01/$FILE/HCAI%20HB%20Dashboard%20Data.xlsx" target="_blank" style="" xpath="1"><img src="/icons/fileatt.gif" border="0" alt="File Attachment Icon"><br>
# HCAI HB Dashboard Data.xlsx</a>
try:
    excel_XPATH = "//a[contains(@href, 'xlsx')]"
    excel_element = driver.find_element(By.XPATH, excel_XPATH)
    excel_element.click()
    time.sleep(5)
except Exception as e:
    # FAILURE CHECK: Handle the case where the element wasn't found
    print(f"Error: Excel file not found! Details: {e}")

# [5] Upload the Excel workbook into pandas
try:
    # Define the expected filename and construct the full path
    file_name = "HCAI HB Dashboard Data.xlsx"
    excel_file_path = os.path.join(download_path, file_name)
    print(f"Loading Excel file: {excel_file_path}")

    # Read all sheets from the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(excel_file_path, sheet_name=None)

    # Iterate through the dictionary of DataFrames
    for sheet_name, df in all_sheets.items():
        # Create a path for the new CSV file inside the 'data' folder
        csv_file_path = os.path.join(download_path, f"{sheet_name}.csv")
        
        # Save the DataFrame to a CSV file, without the pandas index
        df.to_csv(csv_file_path, index=False)
        print(f"  - Sheet '{sheet_name}' saved to '{sheet_name}.csv'")

except Exception as e:
    print(f"An error occurred while processing the Excel file: {e}")
