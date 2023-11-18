from pymongo import MongoClient
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from collections import deque
from tqdm import tqdm
import time

es = Elasticsearch('http://pcentos.hujun.com:9200')
mgclient = MongoClient("pcentos.hujun.com",27017)
db = mgclient['股票信息']
col = db['市场消息']

# 以mongodb中table的_id字段,这样有两个好处：1. mongodb和es数据可以完全对照； 2.es数据在有了id之后就无法产生重复数据。

actions = []
for data in tqdm(col.find({}), total=col.count_documents({})):
    rid = str(data.pop('_id'))
    action = {
        "_id":  rid,
        "_index": '股票市场消息',
        "_source": data
    }

    actions.append(action)
    # Dump x number of objects at a time
    if len(actions) >= 100:
        deque(parallel_bulk(es, actions), maxlen=0)
        actions = []
    time.sleep(.01)









"""
參考這個：
https://segmentfault.com/a/1190000022979256
https://segmentfault.com/a/1190000022949609

https://zhuanlan.zhihu.com/p/85050999
"""


'''

rec = col.find_one({'股票代码':'600622'})

a= str(rec['_id'])

print(a)


mappings = {
      "mappings": {
        "type_doc_test": {              #type_doc_test为doc_type
          "properties": {
            "id": {
              "type": "long",
              "index": "false"
            },
            "serial": {
              "type": "keyword", # keyword不会进行分词,text会分词
              "index": "false" # 不建索引
            },
            #tags可以存json格式，访问tags.content
            "tags": {
              "type": "object",
              "properties": {
                "content": {"type": "keyword", "index": True},
                "dominant_color_name": {"type": "keyword", "index": True},
                "skill": {"type": "keyword", "index": True},
              }
            },
            "hasTag": {
              "type": "long",
              "index": True
            },
            "status": {
              "type": "long",
              "index": True
            },
            "createTime": {
              "type": "date",
              "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            },
            "updateTime": {
              "type": "date",
              "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"
            }
          }
        }
      }
    }


res = es.indices.create(index = 'index_test',body =mappings)

action ={
              "id": "1111122222",
              "serial":"版本",
              #以下tags.content是错误的写法
              #"tags.content" :"标签2",
              #"tags.dominant_color_name": "域名的颜色黄色",
              #正确的写法如下：
              "tags":{"content":"标签3","dominant_color_name": "域名的颜色黄色"},
              #按照字典的格式写入，如果用上面的那种写法，会直接写成一个tags.content字段。
              #而不是在tags中content添加数据，这点需要注意
              "tags.skill":"分类信息",
              "hasTag":"123",
              "status":"11",
              "createTime" :"2018-2-2",
              "updateTime":"2018-2-3",
        }


es.index(index="index_test",doc_type="doc_type_test",body = action)
'''