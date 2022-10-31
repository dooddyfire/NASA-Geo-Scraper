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
import os 

options = webdriver.ChromeOptions() 

options.add_argument("download.default_directory={}".format(os.getcwd()))


x = datetime.datetime.now()
month = x.strftime("%m")
day = x.strftime("%d")




#Get bot selenium make sure you can access google chrome
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.get("https://oceandata.sci.gsfc.nasa.gov/ob/getfile/AQUA_MODIS.2022{}{}T065000.L2.SST.NRT.nc".format(month,day))
# login 
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("TharapornBoon")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("B0854241955b")
button = driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
driver.execute_script("arguments[0].click();", button)
time.sleep(20)



driver.close()


print("สำเร็จ")
