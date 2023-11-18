from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.execute_script("document.body.style.transform='scale(0.5)'")

time.sleep(30)

drive.close()
