# python 关键字


## := 用法


此符号:=是Python语言中的赋值运算符(主要称为海象运算符)。简而言之，海象操作符压缩了我们的代码以使其更短。

下面是一个非常简单的例子：

```python
# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")

# with walrus
if (n := 30) > 10:
    print(f"{n} is greater than 10")

``` 
这些代码是相同的(并且输出相同的内容)，但是正如您所看到的，使用walrus操作符的版本被压缩到两行代码中，以使内容更紧凑

那么，为什么要使用海象操作符呢？ 

我自己甚至很少用到这个。我只是使用海象运算符来压缩代码，主要是在使用正则表达式时。

## sorted 函数

funcs = {'square': square, 'cube': cube, }

sorted(funcs)


## 处理标准输入： input函数

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
print(is_leap)