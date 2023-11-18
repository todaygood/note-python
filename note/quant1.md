
# Quant 如何运算百万行的数据？
https://www.zhihu.com/question/20756848

高频交易程序数据库用哪种方式存储数据？
https://www.optbbs.com/forum.php?mod=viewthread&tid=242083


1. 使用redis
2. 使用mangodb
3. 使用 hdfs

pandas则是专门针对金融类计算设计开发的计算库（Python Data Analysis Library），底层使用HDF5格式（一种高效的数据存储格式，对于金融时间序列来说远远优于CSV），
上层提供很多强大的内建函数（统计类的mean，stddev，类SQL的group by，order by等等），而且本身工作在python环境里，
可以直接使用python做编程方面的工作。更值得一提的是HDF5也是matlab支持的存储格式，所以有必要的时候可以无缝迁移到matlab（如果正好有某个算法是matlab提供而python没有的）。需要强调的是python在科学计算方面有巨大的优势，是统治级的语言，像并行计算，GPU之类都有很好的支持，不用担心要自己搭框架。

# 量化回测用什么数据库？ clickhouse

参见对于一些私募、投资机构和个人来说，量化投资研究、回测离不开数据的支持。当数据量达到一定数量，如A股所有频率和种类的数据等等。这时候需要的是对数据有效的储存和管理。今年6月才开源的数据库ClickHouse，为我们提供了福音。ClickHouse来自俄罗斯，又是刚刚开源，社区也是俄语为主。因此，大家对它并不是很熟悉，用的人也不是很多。

战斗民族开源神器ClickHouse：一款适合于构建量化回测研究系统的高性能列式数据库（一）
https://cloud.tencent.com/developer/article/1031187?from=10680

 

战斗民族开源神器ClickHouse：一款适合于构建量化回测研究系统的高性能列式数据库（二）
https://cloud.tencent.com/developer/article/1031193


1000倍！ClickHouse存储A股数据实践
https://cloud.tencent.com/developer/article/1799255

量化回测，苦于MySQL久矣，特别是进行股票日内因子构建分析或全市场因子测试的时候，每当按下回车时，MySQL就跟丢了魂一样，查询费时，大吞吐量读取也非常耗时。虽然MySQL的优化技巧足够写一本书，但这些都需要交给专业的DB工程师去做，量化打工人没有能力更没有时间倒腾这些。那有没有省时省力，高效存储股票行情数据的解决办法呢。



# mongoDB vs ElasticSearch

## MongoDB适合
对服务可用性和一致性有高要求
无schema的数据存储 + 需要索引数据
高读写性能要求, 数据使用场景简单的海量数据场景
有热点数据, 有数据分片需求的数据存储
日志, html, 爬虫数据等半结构化或图片，视频等非结构化数据的存储
有js使用经验的人员(MongoDB内置操作语言为js)

## Elasticsearch适合
已经有其他系统负责数据管理
对复杂场景下的查询需求，对查询性能有要求, 对写入及时性要求不高的场景
监控信息/日志信息检索
小团队但是有多语言服务，es拥有restful接口，用起来最方便
————————————————
版权声明：本文为CSDN博主「时间都哪去了」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kongliand/article/details/108691847


python 实现Web版股票行情界面
https://cloud.tencent.com/developer/article/1531223

干货 | Elasticsearch多表关联设计指南
https://developer.aliyun.com/article/707086


# NLP

https://www.tableau.com/zh-cn/learn/articles/natural-language-processing-examples

HanLP作者何晗老师的新书《自然语言处理入门》详细笔记
https://github.com/NLP-LOVE/Introduction-NLP

https://github.com/crownpku/Awesome-Chinese-NLP


OCR文字识别在股票查询的运用逻辑
深度学习框架  http://www.woshipm.com/ai/2501970.html


如何用大数据炒股
https://cloud.tencent.com/developer/article/1130856?from=article.detail.1930583

飞桨深度学习平台
https://www.paddlepaddle.org.cn/
https://github.com/PaddlePaddle/awesome-DeepLearning

https://www.51cto.com/article/687752.html

nlp入门： https://zhuanlan.zhihu.com/p/292993516

[nltk使用方法](https://blog.csdn.net/asialee_bird/article/details/85936784)

金融开源代码查询： https://gitee.com/explore/stocks?lang=Python

mongodb工具 https://developer.aliyun.com/article/721720

通达信公式转化为python代码 https://gitee.com/xzan/funcat

# todo 

 
jupyter https://jupyter.org/install

使用词嵌入识别公司名称和股票代码  https://zhuanlan.zhihu.com/p/420367519



https://www.cnblogs.com/zhangshuaiyin/p/10979084.html


https://github.com/zhiaozhou/Chinese-Stock-Prediction-Using-Weibo-Baidu-News-Sentiment


# python操作MongoDB


[python mongodb 入门](https://www.runoob.com/python3/python-mongodb-sort.html)
[python mongodb 手册](https://pymongo.readthedocs.io/en/stable/index.html)

https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/ , 右边选择python语言 


选择operator 
https://www.mongodb.com/docs/manual/reference/operator/query/#std-label-query-selectors


pymongo去重: 插入数据时,不存在则插入,存在则不执行
https://blog.csdn.net/weixin_44285988/article/details/99448931
https://www.jianshu.com/p/1cf04f5452c4
https://blog.csdn.net/weixin_30730053/article/details/98788532


python爬虫数据分别存入MySQL、MongoDB、Redis数据的操作
https://blog.csdn.net/weixin_43870646/article/details/105496800




