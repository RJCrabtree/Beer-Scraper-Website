from selenium import webdriver
import pandas as pd 
import csv
import time

driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/1/")

time.sleep(5)

# driver.find_element_by_xpath("//select[@name='alcohol_table_length']/option[text()='100']").click()

parentElement = driver.find_element_by_xpath("/html/body/main/div[3]/div/div[2]/div/table")
elementList = parentElement.find_elements_by_tag_name("td")

beers = []
search_number = 0
count = 0
idkanymore = 0
test = 0

print("starting page 1")

for element in elementList:
    for x in element.find_elements_by_tag_name("a"):
        beers.append((x.text).replace(',',''))
        count +=1
        print(count)

""" print(beers)
print(beers[0]) """

driver.get("//a[text() = " + beers[0] + "]")

driver.close()