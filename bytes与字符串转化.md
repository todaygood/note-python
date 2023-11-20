

Python bytes与字符串转化

「已注销」

于 2019-07-04 10:01:27 发布

7987
 收藏 3
版权
# bytes转字符串方式一
b=b'\xe9\x80\x86\xe7\x81\xab'
string=str(b,'utf-8')
print(string)

# bytes转字符串方式二
b=b'\xe9\x80\x86\xe7\x81\xab'
string=b.decode() # 第一参数默认utf8，第二参数默认strict
print(string)

# bytes转字符串方式三
b=b'\xe9\x80\x86\xe7\x81haha\xab'
string=b.decode('utf-8','ignore') # 忽略非法字符，用strict会抛出异常
print(string)

# bytes转字符串方式四
b=b'\xe9\x80\x86\xe7\x81haha\xab'
string=b.decode('utf-8','replace') # 用？取代非法字符
print(string)

# 字符串转bytes方式一
str1='逆火'
b=bytes(str1, encoding='utf-8')
print(b)

# 字符串转bytes方式二
b=str1.encode('utf-8')
print(b)
————————————————
版权声明：本文为CSDN博主「「已注销」」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/naonaoxiansheng/article/details/94595999


