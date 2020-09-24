from selenium import webdriver
import pandas as pd 
import time
import csv
from csv import reader
from csv import DictReader

driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver")
driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/1/")

def listToString(row):  
    str1 = ""  
    for ele in row:  
        str1 += ele
    str1 = str1.replace("4.4","/")
    str1 = str1.replace(" ", "-") 
    str1 = str1.replace("(","")
    str1 = str1.replace(")","")
    str1 = str1.replace("'","-")
    return str1  
    
with open("beers1.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        driver.find_element_by_link_text((listToString(row)[:-2] + "/")).click()
        # print(listToString(row)[:-2] + "/")

driver.close()