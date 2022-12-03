import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:/Users/lehma/Downloads/chromedriver_win32 (1)/chromedriver.exe')
initials = 'AR'

allNames = []

pageNum = 1
while True:
    driver.get("https://profiles.stanford.edu/browse/vice-provost-for-undergraduate-education?name="+initials[1]+"&p="+str(pageNum))
    names = driver.find_elements(By.TAG_NAME, 'h4')
    numNames = len(names)
    if (numNames == 0):
        break
    for i in range(numNames):
        try:
            allNames.append(names[i].text)
        except:
            driver.refresh()
            names = driver.find_elements(By.TAG_NAME, 'h4')
            allNames.append(names[i].text)
    print("Processed page " +  str(pageNum))
    pageNum += 1

print("Processed " + str(len(allNames)) + " names")

print("matching names: ")
for name in allNames:
    if initials[0] == name[0]:
        print(name)