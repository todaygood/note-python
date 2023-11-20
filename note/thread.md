

最近在练习python多线程编程时发现，在子线程中设置sys.exit()无法退出整个线程，但是如果想达到此目的又不想使用 os._exit()这种暴力的方法，可以使用daemon线程守护。结合网上零星的几篇文章和自己的测试，有如下的理解：

子线程daemon默认跟随主线程
设置daemon=True会标记其为守护线程，如果剩下的线程只有守护线程时，整个python程序都会退出
————————————————
版权声明：本文为CSDN博主「Amchii」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/exmlyshy/article/details/85220762

https://zhuanlan.zhihu.com/p/91601448