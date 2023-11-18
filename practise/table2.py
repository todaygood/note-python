'''
参见 https://blog.csdn.net/Jiajikang_jjk/article/details/80037068
'''

# coding=utf-8
"""
@author: jiajiknag
程序功能： 获取HTML表格并写入CSV文件
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 维基百科的文本编辑器对比词条
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsobj = BeautifulSoup(html)


# 主对比表格是当前页面上的第一个表格
table = bsobj.findAll("table",{"class":"wikitable"})[0]
# 一行
rows = table.findAll("tr")

csvFile = open("wikipedia.csv", 'wt', newline='',encoding='utf-8')
# 写入
writer = csv.writer(csvFile)
try:
    # 遍历
    for row in rows:
        # 创建一个空列表
        csvRow = []
        # 'td'一行中的列，
        for cell in row.findAll(['td', 'th']):
            # 利用函数get_text()获取-添加
            csvRow.append(cell.get_text())
            # 写入
            writer.writerow(csvRow)
finally:
    # 关闭
    csvFile.close()




