'''
获取 http://stock.jrj.com.cn/report/plsj.shtml?to=pc  中的季报预披露时间

'''
import csv
from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR



csvFile=open('预披露时间.csv', mode='w+',newline='',encoding='utf-8')
wr= csv.writer(csvFile)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("http://stock.jrj.com.cn/report/plsj.shtml?to=pc")

table_element=driver.find_element(By.XPATH, '//*[@id="ntabHeader"]/table')
line = table_element.find_element(By.CSS_SELECTOR,'tr')

str_list=[]
for row in line.find_elements(By.CSS_SELECTOR, 'th'):
    str_list.append(row.text)

print("head is :\n",str_list)
wr.writerow(str_list)


table_element=driver.find_element(By.XPATH, '//*[@id="ntabBody"]/table')
lines = table_element.find_elements(By.CSS_SELECTOR,'tr')
for line in lines:
    str_list = []
    for row in line.find_elements(By.CSS_SELECTOR, 'td'):
        str_list.append(row.text)

    wr.writerow(str_list)



#print(str_list)






'''
# 先抓取
df = pd.read_html(f'http://stock.jrj.com.cn/report/plsj.shtml?to=pc', encoding='gbk', header=0)[1]
print(df)
df.to_csv('预披露时间.csv', mode='w', index=False)  # 追加写入

df_table=pd.read_html(table_element)[0]

df_table.to_csv('预披露时间.csv', mode='a+', index=False)  # 追加写入


import pandas as pd
df = pd.read_html(f'http://stock.jrj.com.cn/report/plsj.shtml?to=pc', encoding='gbk', header=0)[1]
for i in range(len(dfs)):
    print("{a} is:".format(a=i),dfs[i])
    
参见 https://stackoverflow.com/questions/58775641/pandas-read-html-not-wait-for-page-loading 
中说 read_html只能抓取html静态页面中的table， 如果是JS程序产生的table，只能使用selenium
    
'''




