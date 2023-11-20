
## QLineEdit密码显示

https://blog.csdn.net/tk01044242_1/article/details/78298743

## QDialog

Qt中使用QDialog来实现对话框，QDialog继承自QWidget，对话框分为两种，一种是模态对话框、 另一种是非模态对话框。即阻塞和非阻塞对话框，而模态对话框又有两种：应用程序级别的和窗口级别的，分别指完成对话框之前阻塞整个应用和阻塞关联窗口。exec（） 和  open（） 分别为应用程序级别和窗口级别的模态对话框，show（）则为非模态对话框。

QDialog::show(): 非模态，非阻塞的。

QDialog::exec(): 模态 ，阻塞，整个系统阻塞掉。

QDialog::open(): 窗口模态，只会阻塞一个窗口，而不是将整个系统阻塞掉。

如果使用exec（）默认为模态的。如果用show（）需要设置setModel（true）才是模态的。

exec() 是一个循环时间函数，

当调用

accept()（返回QDialog::Accepted），表示确定

reject()（返回QDialog::Rejected），表示取消

done(r)（返回r），

close()（返回QDialog::Rejected），

hide()（返回 QDialog::Rejected），

destory()（返回QDialog::Rejected）。

还有就是delete 自己的时候也会返回 QDialog::Rejected（destory（）就会delete自己）

2.销毁对象
1）调用close()并不会销毁对象，设置属性setAttribute（Qt::WA_DeleteOnClose）才会在close后销毁对象。如果没有设置属性，则效果跟hide()、setVisible()差不多，都只是起一个隐藏作用。

2）deleteLater 可在事件循环结束时销毁对话框(需要使用exec()开始事件循环)。
————————————————
版权声明：本文为CSDN博主「Mr.codeee」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wzz953200463/article/details/101101135


## QT教程 

最近在学习Python GUI开发，之前一直都是做的C++ GUI开发，用到的大部分是框架，主要有MFC、DuiLib和Qt。哦，如果想省时省力，可以使用Qt WebEngine+H5开发界面哦，要是你Web前端不错的话，捣鼓一下就可以做出炫酷的界面。如果想用MFC做出好看的界面，除非你要重绘许多控件，那你还不如拿这个时间成本来学习DuiLib和Qt呢！

使用PyQt 5开发界面，真的很方便，不用写太多代码，20行左右就可以出现简单的带图标GUI
————————————————
版权声明：本文为CSDN博主「吴来斌」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_24880013/article/details/89422078

[CSDN QT入门](https://blog.csdn.net/wzz953200463/category_10815706.html)


通过 Qt 实现的著名软件包括 3D 建模和动画软件 Autodesk Maya 、暴雪公司开发的游戏对战平台 battle.net 、三维虚拟地图软件 Google 地球、虚拟机软件 VirtualBox 、 EA 出品的著名赛车类游戏极品飞车等众多著名软件。

## Qt WebEngine+H5

混合开发方面

重新设计了与 HTML5 Web 交互的引擎，推出基于 Chromium 的 Qt WebEngine ，从而实现了 HTML5 和 QT 混合开发的支持，另外，Qt WebEngine 还提供了跨平台的 API，集成了 QT 的图像库
该版本是最后一个支持 WebKit 的版本，在今后发布的版本中将停止对于 WebKit 的支持
在商业授权协议和 LGPLv3 授权协议下推出了 Qt WebView，且支持 iOS 和 Android，从实现了利用原生的操作系统浏览器引擎整合网页内容
新增了 Qt WebChannel 模块，该模块提供了在 QML/C++ 和 HTML/Javascript 之间的一个简单、易用的桥接，从而使得开发能够使用 Qt 和 Web 技术进行混合开发


https://www.infoq.cn/article/2014/12/qt-5.4-release-html


## QT程序发布打包 

还是使用pyinstaller, 参见https://zhuanlan.zhihu.com/p/104789440

包含QSS样式文件 ，待学习。

pyinstaller参数https://blog.csdn.net/qq_39621009/article/details/122308590



## 自动升级

https://cloud.tencent.com/developer/article/1663398

通过这个功能的实现思路，我们也可以把软件上的一些文本和图片，通过远程来及时更新，如二维码等等。