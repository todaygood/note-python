

https://python3-cookbook.readthedocs.io/zh_CN/latest/



## python 跨平台

python跨平台是指python程序不需要编译，直接用解释器运行，但是解释器（就是安装的python环境）本身在不同平台是不一样的，需要编译

### 如何解决python程序部署的问题？ 

1. 使用conda，参见 https://zhuanlan.zhihu.com/p/134306869

2. pip生成批量离线安装包(whl文件)：

pip wheel --wheel-dir=./tmp/packages -r requirements.txt

参见： https://blog.csdn.net/weixin_39604350/article/details/111459737

3. 使用docker 

