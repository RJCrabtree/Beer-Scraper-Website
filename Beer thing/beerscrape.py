from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import os


hidden = True

coptions = Options()
if hidden:
    coptions.add_argument("--headless")
    coptions.add_argument("--disable-gpu")
    coptions.add_argument("--window-size=1920x1080")
    coptions.add_argument("--log-level=3")
coptions.add_experimental_option('excludeSwitches', ['enable-logging'])
if os.path.isfile("chromedriver.exe"):
    driver = webdriver.Chrome("chromedriver.exe", options=coptions)
else:
    driver = webdriver.Chrome("C:\\Users\\RJ_cr\\OneDrive\\Desktop\\chromedriver", options=coptions)

#driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/1/")

#time.sleep(5)

# driver.find_element_by_xpath("//select[@name='alcohol_table_length']/option[text()='100']").click()

beers = {}
alcholpercentages = {}
pages = 4
lastcount = 0

for page in range(1, pages):
    print("Starting page " + str(page))
    driver.get("https://www.thebeerguy.ca/alphabetical-list-of-beer/page/" + str(page) + "/")
    time.sleep(3)
    parentElement = driver.find_element_by_xpath("/html/body/main/div[3]/div/div[2]/div/table")
    elementList = parentElement.find_elements_by_tag_name("td")
    for element in elementList:
        for x in element.find_elements_by_tag_name("a"):
            beers[((x.text).replace(',',''))] = x.get_attribute("href")
    print("Page " + str(page) +" Total - " + str(len(beers) - lastcount))
    lastcount = len(beers)

print("Total Beers - " + str(len(beers)))
print("First record:")
print(list(beers.keys())[0] + " - " + beers[list(beers.keys())[0]])   

input("Hit enter to start grabbing percentages...")

f = open("beers.csv","w")
count = 0
for name in list(beers.keys()):
    try:
        driver.get(beers[name])
        cat = driver.find_element_by_xpath("/html/body/main/div[3]/div/div/ul/li[3]/a").text
        subcat = driver.find_element_by_xpath("/html/body/main/div[3]/div/div/ul/li[4]/a").text
        percent = driver.find_element_by_xpath("/html/body/main/div[4]/div/div/div[1]/div/div[2]/div[1]/div[2]/p[3]").text.split(": ")[1]
        f.write(name + ", " +  cat  + ", " +  subcat  + ", " + percent + "\n") 
        count += 1
        if count % 50 == 0:
            print(str(count) + " done")
    except:
        f.write(name + ",N/A, N/A, 0.0%\n")
        print("Error on beer " + str(count+1) + "with link: " + beers[name])

print("Done")
    
driver.close()