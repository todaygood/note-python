# Python知识点总结2

## Python 文字到声音转换
Python模块---制作属于自己的有声小说， pysstx3模块介绍 https://www.cnblogs.com/cherish-hao/p/12690637.html

## 时间 ，日历时间。

时间日期类型在Python中主要有两个模块：time模块和datetime模块

time模块:是基于Unix Timestamp（时间戳）实现的，所能表述的范围被限定在1970-2038年之间；
时间戳：是指格林尼治时间1970年01月01日00时00分00秒起至现在的总秒数，结果是一个浮点数。

https://www.py.cn/faq/python/20334.html

互联网上经常传输这个时间戳
```python
a=1651308098
print(time.ctime(a))
```

## Python import 问题 

总结：小规模的程序尽量用绝对路径， 大规模的包/程序 再用相对路径

参见：python相对导入常见问题和解决方案
https://blog.51cto.com/u_14201949/4026370

[Python __init__.py 文件使用](https://www.cnblogs.com/BlueSkyyj/p/9415087.html)

问题可以学习：
https://blog.csdn.net/SKY453589103/article/details/78863050?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&utm_relevant_index=1

相对导入应当使用在包（由多个或多目录层级 *.py 模块组成）内模块中的 import 语句，用于内部模块功能之间的相互调用，而包内模块及功能则应当通过包外脚本调用。

因此你应该这样思考和解决：当前的代码结构真的存在包-模块层级关系吗？如果存在，你应当在包外部通过脚本引用任意包-模块功能；如果不存在，你应当使用绝对导入直接导入同级目录模块。
————————————————
版权声明：本文为CSDN博主「jaredyam」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43958105/article/details/114012590

[在Python中以绝对路径或者相对路径导入文件的方法](https://blog.csdn.net/xiongchengluo1129/article/details/80453599?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ETopBlog-1.topblog&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ETopBlog-1.topblog&utm_relevant_index=1)

Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Connection: keep-alive
Content-Type: application/json;charset=utf-8

sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1

[Python项目如何合理组织规避import天坑](https://zhuanlan.zhihu.com/p/78247846)

## execJs 

https://github.com/meatjam/PyExecJS


## 可变参数

可变参数：就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个

在参数前面加上*就是可变参数。在函数内部，参数numbers接收得到的是一个tuple，调用该函数时，可以传入任意个参数，包括0个参数：

https://blog.csdn.net/u012005313/article/details/48156887


### 默认参数

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

    