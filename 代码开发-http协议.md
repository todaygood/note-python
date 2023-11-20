## HTTP 请求头中的Content-Type

在HTTP请求中，我们每天都在使用Content-Type来指定不同格式的请求信息，但是却很少有人去全面了解Content-Type中允许的值有多少，因此这里来了解一下Content-Type的可用值，以及在Spring MVC中如何使用它们来映射请求信息。

什么是Content-Type

要知道什么是Content-Type，首先要了解什么是Internet Media Type。Internet Media Type即互联网媒体类型，也叫做MIME类型，使用两部分标识符来确定一个类型。在HTTP协议消息头中，使用Content-Type来表示具体请求中的媒体类型信息，意思就是说，Content-Type是Internet Media Type在HTTP协议中的别称。

Content-Type的格式

type/subtype(;parameter)? type
上面是Content-Type的格式，可以拆解为三个部分，分别是主类型（type）、子类型（subtype）和参数（parameter）。

主类型（type）

主类型可以是任意的字符串，比如text。如果是*号则代表所有类型。

子类型（subtype）

子类型可以是任意的字符串，比如html。如果是*号则代表所有类型。

参数（parameter）

参数是可选的，可以在Content-Type中加入一些特殊的参数，比如Accept请求头的参数，常见的有用于设置字符编码的charset参数。

Content-Type: text/html;charset:utf-8;

Content-Type中常见的媒体格式类型

以text开头的媒体格式类型：

text/html： HTML格式。

text/plain：纯文本格式。

text/xml：  XML格式。

以image开头的媒体格式类型：

image/gif：gif图片格式。

image/jpeg：jpg图片格式。

image/png：png图片格式。

以application开头的媒体格式类型：

application/xhtml+xml：XHTML格式。

application/xml： XML数据格式。

application/atom+xml：Atom XML聚合格式 。

application/json： JSON数据格式。

application/pdf：pdf格式 。

application/msword： Word文档格式。

application/octet-stream： 二进制流数据（如常见的文件下载）。

application/x-www-form-urlencoded： <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）。

另外还有一种常见的媒体格式是上传文件之时使用的：

multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式。

以上就是我们在日常的开发中，经常会用到的若干Content-Type的内容格式。
————————————————
版权声明：本文为CSDN博主「沐沐185」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_67642008/article/details/127352126



## flask中的session 

request和session 都是对应每一个请求的。

&session=0x15c040c41c0, session=<SecureCookieSession {'username': 'hujun', 'uid': 1}>
&session=0x1c5e67c41c0, session=<SecureCookieSession {'username': 'hujun2', 'uid': 2}>


assert后面的不要加括号； 


根据手册，在CPython中，id()是变量的实际内存地址。如果您希望它为十六进制格式，请在其上调用hex()。

 
x = 5
print hex(id(x))
这将打印x的内存地址


## Java 拦截器

https://blog.csdn.net/fwdwqdwq/article/details/126114268?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-1-126114268-blog-123972827.pc_relevant_multi_platform_whitelistv4&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-1-126114268-blog-123972827.pc_relevant_multi_platform_whitelistv4&utm_relevant_index=1

Java里的拦截器是动态拦截Action调用的对象，它提供了一种机制可以使开发者在一个Action执行的前后执行一段代码，也可以在一个Action执行前阻止其执行，同时也提供了一种可以提取Action中可重用部分代码的方式。

flask使用装饰器实现登录验证

https://blog.csdn.net/kylinxjd/article/details/95343323



##  用flask 写接口，如何获取请求参数数据呢。

1、get 参数

 if request.method == "get":
 	text = request.args.get('text')
 
2、post 参数

 if request.method == "POST":
        id=request.form.get('id')
        word=request.form.get('word')


版权声明：本文为CSDN博主「东华果汁哥」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u013421629/article/details/102917473



## 从有状态变成无状态,使用token 

https://zhuanlan.zhihu.com/p/560102384

https://blog.csdn.net/ousuixin/article/details/94053454


https://blog.csdn.net/qq_44198436/article/details/112100732



## Http协议内容 

https://developer.aliyun.com/article/618177
https://httpie.io/