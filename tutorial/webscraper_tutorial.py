## TUTORIAL from: https://github.com/Codecademy/articles/blob/main/web-scrape-with-beautiful-soup-and-selenium/olympic_data.py
## https://www.codecademy.com/article/web-scrape-with-selenium-and-beautiful-soup

import os, time, csv, re
from selenium import webdriver
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

## Step 1: Launching a browser using Selenium
driver = Chrome()
driver.get("http://www.olympedia.org/statistics/medal/country")

## Step 2: Retrieving  form elements
# dropdowns
year_dd = driver.find_element(by="id", value = "edition_select")
gender_dd = driver.find_element(by="id", value = "athlete_gender")

# options
year_options = year_dd.find_elements(by="tag name", value = "option")
gender_options = gender_dd.find_elements(by="tag name", value = "option")

## Step 3: Navigating the website using BeautifulSoup & Parsing the HTML content

usa_lst = []

for gender in gender_options[1:]:  # index 0 is omitted because it contains placeholder txt 
   gender.click() 
   gender_val = gender.get_attribute("text")
  
   for year in year_options[2:]: # skipping first two options to start with 1900  
       year.click() 
       time.sleep(0.5)  # Allow time for the page to update
       the_soup = BeautifulSoup(driver.page_source, 'html.parser')
       year_val = year.get_attribute("text")
       
       head = the_soup.find(href=re.compile('USA'))
       
       if head:
            medal_values = head.find_all_next('td',limit=5)
            val_lst = [x.string for x in medal_values[-4:]]
       else:
            # If no 'USA' link is found, default to 0 for all medals.
            val_lst = ['0'] * 4
        
       # print(year_val, gender_val, val_lst)
       val_lst.append(gender_val)
       val_lst.append(year_val)
       usa_lst.append(val_lst)
       #print(usa_lst)
        

# Close the browser session 
driver.quit()

## Step 4: Saving the data as CSV 
output_f = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_f)
for row in usa_lst:
     output_writer.writerow(row)
output_f.close()     
print('done')