from datetime import datetime
import time
import pymongo
import pprint
import pandas as pd
import re
import json




a=int(time.time())
print(a)



"""
db_client = pymongo.MongoClient('pcentos.hujun.com', 27017)
db_instance = db_client['test1-db']
db_table = db_instance['test1']



dicts = {'one': [1, 2, 3], 'two': [2, 3, 4], 'three': [3, 4, 5]}
df = pd.DataFrame(dicts)

dict_array=json.loads(df.T.to_json()).values()
print(dict_array)

db_table.insert_many(dict_array)



a=datetime.strptime('2022-04-29 00:00:00','%Y-%m-%d %H:%M:%S')
print(a)

a='2022-04-29 00:00:00'
b='2022-04-28'

print(a>b)

line = "Cats *are smarter than dogs"

pattern = re.compile(r'\*')

#b=re.findall(pattern,line)
#print(b)

a= re.sub(pattern,'中国',line)
print(a)

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)


print(matchObj.groups())
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))





title='快讯：芯片板块持续走强'

if title.startswith('快讯：'):
    print(title)

kuaixun="【快讯：芯片板块持续走强】财联社4月29日电，三环集团、东芯股份、派瑞股份、弘信电子涨超10%，汇顶科技、江海股份涨停，中晶科技、广东骏亚、麦捷科技、泰晶科技、英集芯、扬杰科技、赛微电子等涨超8%。消息面上，三星电子第一季度净利润超预期，得益于芯片需求稳健。"

print(kuaixun.split(sep='、'))

import re
def parse_sz_stock_name():
    a='<a href=\'http://www.szse.cn/certificate/individual/index.html?code=000001\' target=\'_blank\'><u>南  玻Ａ</u></a>'
    b=a.split(sep='<u>')
    c=(b[1].split(sep='</u>'))[0]
    d=re.sub(r"\s+", "", c)

    print(d)

parse_sz_stock_name()
"""


db_client=pymongo.MongoClient('pcentos.hujun.com',27017)
db_instance= db_client['stock_basic_info']
db_table=db_instance['basic']


'''
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }\

x=db_table.insert_one(mydict)
print(x)

mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

db_table.insert_many(mylist)

mylist2 = [
  { "_id": 6, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 7, "name": "Google", "address": "Google 搜索"},
  { "_id": 8, "name": "Facebook", "address": "脸书"},
  { "_id": 9, "name": "Taobao", "address": "淘宝"},
  { "_id": 10, "name": "Zhihu", "address": "知乎"}
]

y=db_table.insert_many(mylist2)
print(y.inserted_ids)

z = db_table.find_one()
print(z)

x = db_table.find()
for one in x:
    print(one)
    
myquery={"name": {"$regex":"^F"}}

newvalues={"$set":{"alexa": "1230000"}}

x=db_table.update_one(myquery,newvalues)

print(x.modified_count)

mydoc= db_table.find({"name":"Facebook"}).sort([('alexa',pymongo.DESCENDING)])
for x in mydoc:
    pprint.pprint(x)

#myquery={"name": {"$regex":"^F"}}
myquery={}
x = db_table.delete_many(myquery)

print(x.deleted_count)
'''



