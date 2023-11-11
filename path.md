
# 总结： 尽量使用绝对路径



import os 
#1获得当前路径，cwd=current working directory
os.getcwd()

#2获得绝对路径
os.path.abspath()

#3获得当前路径的上级目录路径
os.path.dirname()

#4组合使用，获得当前**文件路径**
os.path.abspath(os.path.dirname(__file__))

#5组合使用，获得当前**工作路径**
os.path.abspath(os.getcwd())

#6**改变当前工作目录到指定路径**
os.chdir()



# 获取当前文件的所在目录
print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))

# 获取当前文件的所在目录
print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))

# 获取当前文件的所在目录
print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])


2.sys.path
模块搜索路径的字符串列表。由环境变量PYTHONPATH初始化得到。是一个目录的列表，sys.path[0]是调用Python解释器的当前脚本所在的目录，即主执行文件的父级目录。例子：如在/user/ybp/a.py的文件a.py中执行：print(sys.path[0])==>/user/ybp，
在命令行执行返回空字符串；

3.注意os.path是系统环境变量，要与上面区分开来，没有os.path[0]，os.path中的一些方法：
(1)os.path.split(path)
将路径名称分成头和尾一对。尾部永远不会带有斜杠。如果输入的路径以斜杠结尾，那么得到的空的尾部。
如果输入路径没有斜杠，那么头部位为空。如果输入路径为空，那么得到的头和尾都是空。
https://docs.python.org/2/library/os.path.html#os.path.split

(2)os.path.realpath(path)
返回特定文件名的绝对路径，可以在命令行中执行。
https://docs.python.org/2/library/os.path.html#os.path.realpath

4.os.getcwd()返回的是当前工作路径，而不一定需要是在脚本里面执行，这个命令相当于pwd，可以在命令行中执行，返回的是绝对路径；
————————————————
版权声明：本文为CSDN博主「py_tester」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/py_tester/article/details/78954034


cron中没有任何环境变量。要注意呀，死过n次人的



使用sys.argv变量获取当前脚本的路径。其中，sys.argv[0]代表当前脚本的文件名，即执行文件的路径。注意，这个方法只适用于在终端中执行Python脚本的情况。如果你在其他环境中运行Python代码，这个方法可能无法获取正确的执行文件路径。