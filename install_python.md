
# 在centos7上安装python3.8

使用软件集合 (SCL) 在 CentOS 7 上安装 Python 3.8

支持
当引入这项技术时，红帽软件集合产品生命周期 - 红帽客户门户网站比，2023-052024-06 似乎是 EOL。
在此之后报告的漏洞和错误的响应可能无法实施。

日志
仓库注册


# yum install -y centos-release-scl

安装
# cat /etc/redhat-release
CentOS Linux release 7.8.2003 (Core)
 
# yum install -y rh-python38 which
# scl enable rh-python38 bash


# which python{,2,3}
/opt/rh/rh-python38/root/usr/bin/python
/usr/bin/python2
/opt/rh/rh-python38/root/usr/bin/python3
 
# ll /opt/rh/rh-python38/root/usr/bin/python*
lrwxrwxrwx. 1 root root     9 Jun 24 10:31 /opt/rh/rh-python38/root/usr/bin/python -> ./python3
lrwxrwxrwx. 1 root root     9 Jun 24 10:31 /opt/rh/rh-python38/root/usr/bin/python3 -> python3.8
-rwxr-xr-x. 1 root root 15280 May 28 09:39 /opt/rh/rh-python38/root/usr/bin/python3.8
 


————————————————
版权声明：本文为CSDN博主「allway2」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/allway2/article/details/121718707

