## PyQt中的信号

[QComboBox的使用](https://zhuanlan.zhihu.com/p/36691866)



PyQt5自动为所有Qt的内置信号定义信号。可以使用pyqtSignal()工厂将新信号定义为类属性。事实上，采用这种方式可以很方便的为我们通过信号传递参数，如：

#无参数的信号
signal_A = pyqtSignal()

#带一个int类型参数的信号
signal_B = pyqtSignal(int)

#带str和int类型参数的信号
signal_C = pyqtSignal(str, int)

#带一个列表类型参数的信号
signal_D = pyqtSignal(list)

#带int和dict类型参数的信号和带str类型参数的信号
signal_E = pyqtSignal([int, dict], [str])
这样就为我们传递各种参数带来了极大的便利性了。

