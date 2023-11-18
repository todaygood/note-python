## Elasticsearch股票分析

Elasticsearch股票分析，参见http://pirrla.com/2017/07/13/es/es_stocks/

### 问题： 如何设置es的分词器？ 

ES中加入hanlp ，参见： https://blog.csdn.net/qq_43692950/article/details/122278275


ES如何设计索引？ https://www.cnblogs.com/zsql/p/14418018.html
 
ES+Kibana 展示股票收益， 参见https://blog.csdn.net/mutex86/article/details/118191751，里面有python操作ES的各种代码片段。 

ES学习笔记，可参见http://pirrla.com/categories/elasticsearch/


## ES中安装使用hanlp 


参见 https://github.com/KennFalcon/elasticsearch-analysis-hanlp
以及 https://zhuanlan.zhihu.com/p/433994401


```bash
[root@pcentos ftpuser]# docker exec -it elasticsearch bash
[root@0c881552d5bd elasticsearch]# ./bin/elasticsearch-plugin -v   install file:///usr/share/elasticsearch/elasticsearch-analysis-hanlp-7.10.1.zip 
-> Installing file:///usr/share/elasticsearch/elasticsearch-analysis-hanlp-7.10.1.zip
-> Downloading file:///usr/share/elasticsearch/elasticsearch-analysis-hanlp-7.10.1.zip
[=================================================] 100%?? 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@     WARNING: plugin requires additional permissions     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
* java.io.FilePermission plugins/analysis-hanlp/data/-#plus read,write,delete
* java.io.FilePermission plugins/analysis-hanlp/hanlp.cache#plus read,write,delete
* java.lang.RuntimePermission getClassLoader
* java.lang.RuntimePermission setContextClassLoader
* java.net.SocketPermission * connect,resolve
* java.util.PropertyPermission * read,write
See http://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html
for descriptions of what these permissions allow and the associated risks.

Continue with installation? [y/N]y
-> Installed analysis-hanlp
[root@0c881552d5bd elasticsearch]# 
[root@0c881552d5bd elasticsearch]# exit
docker restart elasticsearch

```

### 更新hanlp完整的数据报

https://blog.csdn.net/qq_43692950/article/details/122278275  中的 “四、数据包的更新”

2. 安装数据包
release包中存放的为HanLP源码中默认的分词数据，若要下载完整版数据包，请查看HanLP Release。

数据包目录：ES_HOME/plugins/analysis-hanlp

注：因原版数据包自定义词典部分文件名为中文，这里的hanlp.properties中已修改为英文，请对应修改文件名


3. hanlp提供的分词方式说明


hanlp: hanlp默认分词

hanlp_standard: 标准分词

hanlp_index: 索引分词

hanlp_nlp: NLP分词

hanlp_n_short: N-最短路分词

hanlp_dijkstra: 最短路分词

hanlp_crf: CRF分词（在hanlp 1.6.6已开始废弃）

hanlp_speed: 极速词典分词