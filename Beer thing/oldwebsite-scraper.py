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

print("starting page 1")

for element in elementList:
    for x in element.find_elements_by_tag_name("a"):
        beers.append((x.text).replace(',',''))
        # print(beers)

print("done page 1")

driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/2/")

parentElement = driver.find_element_by_xpath("/html/body/main/div[3]/div/div[2]/div/table")
elementList = parentElement.find_elements_by_tag_name("td")

print("starting page 2")

for element in elementList:
    for x in element.find_elements_by_tag_name("a"):
        beers.append((x.text).replace(',',''))
        # print(beers)

print("done page 2")



driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/3/")

parentElement = driver.find_element_by_xpath("/html/body/main/div[3]/div/div[2]/div/table")
elementList = parentElement.find_elements_by_tag_name("td")

print("starting page 3")

for element in elementList:
    for x in element.find_elements_by_tag_name("a"):
        beers.append((x.text).replace(',',''))
        # print(beers)

print("done page 3")

driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/4/")

parentElement = driver.find_element_by_xpath("/html/body/main/div[3]/div/div[2]/div/table")
elementList = parentElement.find_elements_by_tag_name("td")

print("starting page 4")

for element in elementList:
    for x in element.find_elements_by_tag_name("a"):
        beers.append((x.text).replace(',',''))
        # print(beers)

print("done page 4")



with open("beers.csv", "w") as f:
    for x in beers:
        f.write(x + ", " + "4.4\n")