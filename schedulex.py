import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 
import datetime
import schedule 


def first_file(): 
    options = webdriver.ChromeOptions() 



    x = datetime.datetime.now()
    month = x.strftime("%m")
    day = x.strftime("%d")




    #Get bot selenium make sure you can access google chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://oceancolor.gsfc.nasa.gov/cgi/browse.pl?sen=amod")

    driver.find_element(By.CSS_SELECTOR,"input[name='n']").send_keys("13.6")
    driver.find_element(By.CSS_SELECTOR,"input[name='w']").send_keys("99.92")
    driver.find_element(By.CSS_SELECTOR,"input[name='e']").send_keys("101")
    driver.find_element(By.CSS_SELECTOR,"input[name='s']").send_keys("12.5")
    driver.find_element(By.CSS_SELECTOR,"input[value='Find swaths']").click()

    curr_url = driver.current_url
    print(curr_url)

    driver.find_element(By.XPATH,"/html/body/center/table[2]/tbody/tr[1]/td[1]/a").click()

    #download
    driver.find_element(By.XPATH,"/html/body/center/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[3]/th/a").click()

    # login 
    driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("TharapornBoon")
    driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("B0854241955b")
    button = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(20)




    #driver.find_element(By.XPATH,"/html/body/center/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[3]/th/a").click()

    #Make sure you have already eliminate recapcha


    driver.close()


    print("L2.OC.NRT.nc สำเร็จ")


def second_file():

    options = webdriver.ChromeOptions() 

    options.add_argument("download.default_directory={}".format(os.getcwd()))


    x = datetime.datetime.now()
    month = x.strftime("%m")
    day = x.strftime("%d")




    #Get bot selenium make sure you can access google chrome
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    driver.get("https://oceancolor.gsfc.nasa.gov/cgi/browse.pl?sen=amod")

    driver.find_element(By.CSS_SELECTOR,"input[name='n']").send_keys("13.6")
    driver.find_element(By.CSS_SELECTOR,"input[name='w']").send_keys("99.92")
    driver.find_element(By.CSS_SELECTOR,"input[name='e']").send_keys("101")
    driver.find_element(By.CSS_SELECTOR,"input[name='s']").send_keys("12.5")
    driver.find_element(By.CSS_SELECTOR,"input[value='Find swaths']").click()

    curr_url = driver.current_url
    print(curr_url)

    driver.find_element(By.XPATH,"/html/body/center/table[2]/tbody/tr[1]/td[1]/a").click()
    # download second file (ไฟล์ที่ 5)
    driver.find_element(By.XPATH,"/html/body/center/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[5]/th/a").click()



        # login 
    driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("TharapornBoon")
    driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("B0854241955b")
    button = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(20)



    driver.close()


    print("L2.SST.NRT สำเร็จ")


schedule.every(9).seconds.do(first_file)

schedule.every(20).seconds.do(second_file)

#schedule.every().day.at("10:30").do(first_file)
#schedule.every().day.at("10:33").do(second_file)

while True:
    schedule.run_pending()
    time.sleep(1)