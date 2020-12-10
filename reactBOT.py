from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\chromedriver\chromedriver.exe" #location of chromedriver
URL = "https://humanbenchmark.com/tests/reactiontime" #https://humanbenchmark.com/tests/reactiontime

driver = webdriver.Chrome(PATH)
sleep(1)
driver.get(URL)
sleep(3)
#Begin Blue: view-splash
#Blue after: view-result
#Green: view-go
#Red: view-waiting

i = 0

try:
    cookie = driver.find_element_by_class_name("Button__StyledButton-a1qza5-0")
    cookie.click()
except:
    print("cookie button not found")
sleep(1)


#click in order to start
try:
    begin = driver.find_element_by_class_name("view-splash")
    begin.click()
    print("Started")
except:
    print("Failed to start")
    driver.quit()

while i<5:
    #find green button
    try:
        green = driver.find_element_by_class_name("view-go")
        green.click()
        i += 1
        print("Green found")
        sleep(1)
    except:
        print("green not found")

    try:
        nexti = driver.find_element_by_class_name("view-result")
        nexti.click()
    except:
        print("next not found")

sleep(10)
driver.quit()






