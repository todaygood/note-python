# mongodb 使用技巧

## 如何在Mogodb中搜索中文？

https://cloud.tencent.com/developer/article/1939649

MongoDB在2.4版中引入全文索引后几经迭代更新已经比较完美地支持以空格分隔的西语，但一直不支持中日韩等语言，社区版用户不得不通过挂接ElasticSearch等支持中文全文搜索的数据库来实现业务需求，由此引入了许多业务限制、安全问题、性能问题和技术复杂性。作者独辟蹊径，基于纯MongoDB社区版（v4.x和v5.0）实现中文全文搜索，在接近四千万个记录的商品表搜索商品名，检索时间在200ms以内，并使用Change Streams技术同步数据变化，满足了业务需要和用户体验需求



## Query 

参见https://cloud.tencent.com/developer/article/1569809  里面的总结很全面。

$elemMatch：要求同时使用多个条件语句来对一个数组元素进行比较判断



# mongodb lookup 函数

https://www.cnblogs.com/jasonminghao/p/13178087.html

详解lookup 

https://www.cnblogs.com/xuliuzai/p/10055535.html



# dataFrame写入mongodb 

  dicts = {'one': [1, 2, 3], 'two': [2, 3, 4], 'three': [3, 4, 5]}
    df = pd.DataFrame(dicts)
    mongo.collection.insert(json.loads(df.T.to_json()).values())
————————————————
版权声明：本文为CSDN博主「data_scientist」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/data_scientist/article/details/54729287


# mongodb lookup 函数

https://www.cnblogs.com/jasonminghao/p/13178087.html

详解lookup 

https://www.cnblogs.com/xuliuzai/p/10055535.html



# dataFrame写入mongodb 

  dicts = {'one': [1, 2, 3], 'two': [2, 3, 4], 'three': [3, 4, 5]}
    df = pd.DataFrame(dicts)
    mongo.collection.insert(json.loads(df.T.to_json()).values())
————————————————
版权声明：本文为CSDN博主「data_scientist」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/data_scientist/article/details/54729287
