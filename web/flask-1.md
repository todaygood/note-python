

## flask 高并发该怎么部署？ 

https://blog.csdn.net/wyyang2/article/details/118610528

Flask 默认是单进程，单线程阻塞的任务模式，在项目上线的时候可以通过nginx+gunicorn 的方式部署flask任务。

app.run()中可以接受两个参数，分别是threaded和processes，用于开启线程支持和进程支持。

1.threaded : 多线程支持，默认为False，即不开启多线程;
2.processes：进程数量，默认为1.


https://zhuanlan.zhihu.com/p/337749105

https://www.rgozi.com/post/flask%E9%83%A8%E7%BD%B2%E6%96%B9%E5%BC%8F%E5%AE%9E%E8%B7%B5/


## PyQT5中启动外部程序

一、启动外部程序的两种方式：

（1）一体式：void QProcess::start(const QString & program, const QStringList & arguments, OpenMode mode = ReadWrite)

        外部程序启动后，将随主程序的退出而退出。


（2）分离式： void  QProcess:: startDetached( const QString & program, const QStringList & arguments, const QString & workingDirectory = QString(), qint64 * pid = 0 )
        外部程序启动后，当主程序退出时并不退出，而是继续运行。

二、Synchronous Process API （同步进程API）
    QProcess提供了一系列的函数以提到事件循环来完成同步操作：
（1）waitForStarted()          : 阻塞，直到外部程序启动
（2）waitForReadyRead()    : 阻塞，直到输出通道中的新数据可读
（3）waitForBytesWritten()  : 阻塞，直到输入通道中的数据被写入
（4）waitForFinished()        : 阻塞，直到外部程序结束
如果在主线程（QApplication::exec()）中调用这些函数，可能会造成当前用户界面不响应。
————————————————
版权声明：本文为CSDN博主「kucoffee12」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kucoffee12/article/details/75200101


PyQt5中如何调用外部exe，并获取返回数据  https://blog.csdn.net/s11092114/article/details/97136005