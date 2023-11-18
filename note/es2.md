
# ES 内存设置

es内核使用lucene，lucene本身是单独占用内存的，并且占用的还不少，官方建议设置es内存，大小为物理内存的一半，剩下的一半留给lucene。

https://www.programminghunter.com/article/66141571812/
```bash
# Linux:

NODE_OPTIONS="$NODE_OPTIONS --max-old-space-size=400"
# 设置200的话，kibana能够起来但是无法访问
```

[在较小内存的机器上运行Elasticsearch与Kibana](https://cloud.tencent.com/developer/article/1464483)
[ElasticSearch系列（七）es内存大小设置](https://blog.csdn.net/csdn_20150804/article/details/107917560)

## es 内存背景

es 是java应用，要设置java堆内存, -Xms 


##  Kibana 内存设置的相关背景

kibana是一个基于NodeJS的单页web应用。而NodeJS则是基于Chrome V8引擎的。V8引擎对于内存的使用是有限制的，默认情况下，64位系统下约为1.4GB，32位系统下约为0.7GB。

V8 为 Node.js 应用，默认只会分配了大概 1400 MB（仅本地测试的结果） 的内存空间。
超出了这个限额，就会内存溢出。
参见 [ Node 内存溢出与 old-space 大小调整](https://www.jianshu.com/p/88d229ebae1c) 

V8 的垃圾回收机制也是与时俱进的，
最近的一些进展，可参考 Trash talk: the Orinoco garbage collector，
上面介绍的内容大同小异。


[kibna内存的环境变量](https://github.com/elastic/kibana/issues/9006)



