from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR

'''
1. 从上海证交所获取龙虎榜数据  "http://www.sse.com.cn/disclosure/diclosure/public/dailydata/"
2. 从深圳证交所获取龙虎榜数据

'''





driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://www.szse.cn/disclosure/deal/public/")
button=driver.find_element(By.CLASS_NAME,"btn-default-excel.btn-default-hasicon")
button.click()

print("已下载文件：竞价交易公开信息.xlsx")

#driver.close()



'''

#wait = WebDriverWait(driver,2)
driver.get("http://www.baidu.com/")
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
# 打印数据内容
print(data)

# data=driver.find_element(By.CLASS_NAME,"btn-default-excel btn-default-hasicon").text



ac= driver.find_element(By.CLASS_NAME,"btn-default-excel btn-default-hasicon")

ActionChains(driver).move_to_element(ac).click(ac).perform()
'''

