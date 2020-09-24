from selenium import webdriver
import pandas as pd 
import csv
import time
from itertools import zip_longest


driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("http://www.swipes.co.uk/beerlist.cgi")

parentElement = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table")
elementList = parentElement.find_elements_by_tag_name("tr")

beers1 = []

print("starting the beer column")

for element in elementList:
    if len(element.find_elements_by_tag_name("td")) > 2 :
        name = element.find_elements_by_tag_name("td")[0].text      
        strength = element.find_elements_by_tag_name("td")[3].text
        beers1 = [name, strength]
                
        with open('beers1.csv', 'a', newline="") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(beers1)
           
print("finished adding to csv file")

driver.close()