from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from selenium.webdriver.common.by import By

URL = "https://humanbenchmark.com/tests/reactiontime" #https://humanbenchmark.com/tests/reactiontime
print("opening driver")
driver = webdriver.Chrome()
print("sleeping for 1 seconds")
sleep(1)
print("get url")
driver.get(URL)
print("sleeping for 5 seconds")
sleep(5)
#Begin Blue: view-splash
#Blue after: view-result
#Green: view-go
#Red: view-waiting

i = 0

# //*[@id="qc-cmp2-ui"]/div[2]/div/button[2]
try:
    cookie = driver.find_element(By.XPATH, "//*[@id=\"qc-cmp2-ui\"]/div[2]/div/button[2]")
    cookie.click()
    print("Cookie button clicked")
except:
    print("cookie button not found")
print("sleeping for 3 seconds")
sleep(3)


#click in order to start
try:
    print("Finding start screen")
    begin = driver.find_element(By.CLASS_NAME, "view-splash")
    begin.click()
    print("Started")
except:
    print("Failed to start")
    print("exiting")
    driver.quit()
    sleep(1)
    sys.exit()

while i<5:
    #find green button
    try:
        green = driver.find_element(By.CLASS_NAME, "view-go")
        green.click()
        i += 1
        print("Green found")
        sleep(1)
    except:
        print("green not found")

    try:
        nexti = driver.find_element(By.CLASS_NAME, "view-result")
        nexti.click()
        print("sleeping vfor 3 seconds")
    except:
        print("next not found")

sleep(10)
driver.quit()






