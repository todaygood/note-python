# ES 干啥用：全文搜索

ElasticSearch（ES）作为一款优秀的分布式搜索分析引擎，越来越收到很多大型互联网公司的关注，像小米、滴滴出行、携程旅游、阿里云和腾讯云都在使用ElasticSearch。

大数据分析搜索利器 

最著名的公司就是github，它采用ES作为搜素引擎对代码进行搜索，虽然它是一款分布式搜索引擎，但是它强大的查询、分析和聚合能力使他与数据库的边界越来越模糊。因此很多大公司都喜欢用ES来存储日志或其他业务数据。最常见的结合就是通过kafka、redis来作数据源，logstash进行转化，ES对数据进行存储、kibana对数据进行展示，ES+logstash+kibana(ELK)一体化的日志分析、业务指标分析。
————————————————
版权声明：本文为CSDN博主「heshengfu1211」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/heshengfu1211/article/details/108699056

[知乎：做一个搜索引擎很难吗？](https://www.zhihu.com/question/27214801)

[分词器的介绍和使用](https://blog.csdn.net/vincent_wen0766/article/details/109244738)

[ElasticSearch 分词器，了解一下](https://zhuanlan.zhihu.com/p/111775508)

[Docker 安装 ElasticSearch和安装IK分词器](https://zhuanlan.zhihu.com/p/257867352)


ES就是以JSON格式存储存储数据的；

支持在线分析、实时分析，ES是基于存储、查询、聚合分析和可视化于一体的解决方案

## ES原理介绍 

https://blog.csdn.net/vic_torsun/article/details/115047177

https://www.cnblogs.com/zhangyafei/p/11028927.html

https://zhuanlan.zhihu.com/p/94181307

## 应用： Elasticsearch+Kibana展示爬虫数据

https://zhuanlan.zhihu.com/p/402831328

## 分词器

https://blog.csdn.net/adnb34g/article/details/87911995
对命名实体识别要求较高的可以选择HanLP，根据说明其训练的语料比较多，载入了很多实体库，通过测试在实体边界的识别上有一定的优势。


