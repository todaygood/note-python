# 认识web开发

[node.js是用来开发前端还是后端？](https://zhuanlan.zhihu.com/p/360005641)

我们知道Web的开发体系中，分成前端，后端，工具，三个主要的领域。

- 前端主要由由浏览器，HTML+CSS+浏览器端JS完成。
- 后端主要是由Web服务器，数据库，动态脚本语言，其它的业务服务器等组成。
- 还有就是很多基础设计与便利资料，我们可以统称为工具。比如源码管理，编辑器，数据库备份，加密，解密，防火墙等一系列的工具。

Node一开始只是服务器端的js，但是现在的说法是node.js已经是js的一个运行时了。它的核心是event driven, non blocking I/O，以及主要由npm构建的模块体系。
所以node.js本身与前端并没有关系，他是一个运行时.

node.js可以辅助前端开发
尽管nodejs不属于前端，但是node.js因为使用的语言是js。所以可以很好的辅助前端开发.

## html中可以嵌入javascript文件，那可以嵌入python代码吗？

用“纯HTML”是没有办法做到这一点的。HTML只是一种布局语言；它几乎没有任何功能可以满足您的需要。你需要某种脚本语言。

虽然有一些浏览器插件可以直接将Python作为脚本语言嵌入其中，但大多数用户都不会安装这样的插件；您甚至可能无法为自己的浏览器找到最新的插件。
事实上，你可以得到的是：几乎所有浏览器中都有JavaScript（或者，如果你想从技术上讲，“ECMAscript”）。

Silverlight实际上允许您运行（Iron）Python代码，尽管将代码从命令行Python环境转换为浏览器脚本Silverlight环境还需要一些工作。同样，Java允许您运行Jython代码。
另外两个需要将代码移植到另一种语言。没有人会帮你这么做；你需要自己学习JavaScript。
参见： https://blog.csdn.net/weixin_39694264/article/details/110336766

所以JavaScript是一个写前端的语言，用来生成动态网页。


## 为何现在前端开发也使用Node.js 

作者：super_wei
链接：https://www.jianshu.com/p/6ed0f7bd44b3
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

传统的js是运行在浏览器上的，因为浏览器内核分为两个部分:

- 渲染引擎---复制渲染HTML和CSS,
- JavaScript 引擎---负责运行 JavaScript, Chrome 使用的 JavaScript 引擎是 V8，它的速度非常快且性能好。

相对于传统的JavaScript来说，Node.js 是一个运行在服务端的框架，它的底层就使用了 V8 引擎。我们知道 Apache + PHP 以及 Java 的 Servlet 都可以用来开发动态网页，Node.js 的作用与他们类似，只不过是使用 JavaScript 来开发，它大大提升了开发的性能以及便利。



为什么学习 JavaScript?
JavaScript 是 web 开发人员必须学习的 3 门语言中的一门：

HTML 定义了网页的内容
CSS 描述了网页的布局
JavaScript 控制了网页的行为

## Npm install 

https://segmentfault.com/a/1190000021468231

npm install moduleName # 安装模块到项目目录下
 
npm install -g moduleName # -g 的意思是将模块安装到全局，具体安装到磁盘哪个位置，要看 npm config prefix 的位置。
 
npm install -save moduleName # -save 的意思是将模块安装到项目目录下，并在package文件的dependencies节点写入依赖。
 
npm install -save-dev moduleName # -save-dev 的意思是将模块安装到项目目录下，并在package文件的devDependencies节点写入依赖。




## issue  express服务在第1次request之后就无响应

用node的时候总是请求半天没反应，然后在命令行按一次ctrl+c又好了；

可能是使用windows powershell的原因，看了下面这个博客改为用git的命令行就不会有这种问题了

https://www.cnblogs.com/zifeiy/p/10213612.html
————————————————
版权声明：本文为CSDN博主「真是个老机灵鬼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41792345/article/details/96288933

