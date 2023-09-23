# 总结python字符串 


1、字符串前加 u
例：u"我是含有中文字符组成的字符串。"

作用：

后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。


2、字符串前加 r
例：r"\n\n\n\n”　　# 表示一个普通生字符串 \n\n\n\n，而不表示换行了。

3、字符串前加 b
例: response = b'<h1>Hello World!</h1>'     # b' ' 表示这是一个 bytes 对象

作用：

b" "前缀表示：后面字符串是bytes 类型。

用处：

网络编程中，服务器和浏览器只认bytes 类型数据。

如：send 函数的参数和 recv 函数的返回值都是 bytes 类型

附：

在 Python3 中，bytes 和 str 的互相转换方式是

str.encode('utf-8')

bytes.decode('utf-8')
 


4. f"{}"

python的字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样. 

格式化的字符串文字前缀为’f’和接受的格式字符串相似str.format()。它们包含由花括号包围的替换区域。替换字段是表达式，在运行时进行评估，然后使用format()协议进行格式化。

formatted string literals, 以 f 开头，包含的{}表达式在程序运行时会被表达式的值代替。

b=[1,2,3]
print(f"b={b}")

 



## all函数

all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

元素除了是 0、空、None、False 外都算 True。

函数等价于：

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True



## chatGPT 

<< AI时代Excel数据分析提升之道>>

AI时代Excel数据分析提升之道：知识精进+学习答疑+上机实训+综合实战+ChatGPT应用，零基础入门，极速提升数据分析效率！

卖点

（1）零基础入门宝典，由浅入深讲解，无须额外的背景知识即可学习掌握。

（2）内容系统全面，可帮助读者快速了解使用Python进行Excel数据分析的基本语法并掌握开发能力。

（3）理论与实践相结合，每个理论都有对应的代码示例，读者参考代码示例完成编写，就可以看到实践效果。

（4）本书配有实训与问答，方便读者阅读后尽快巩固知识点，做到举一反三、学以致用。

（5）AI前沿产品ChatGPT+Python进行Excel数据分析，大幅学习和分析的效率


