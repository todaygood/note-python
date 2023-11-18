
# python requests 如何绕过系统的代理

https://segmentfault.com/q/1010000007245089

两种方式:
session = requests.Session()
session.trust_env = False
response = session.get('http://ff2.pw')
或者:
proxies = { "http": None, "https": None}
requests.get("http://ff2.pw", proxies=proxies)
都可以绕过系统设置的代理


# pip install时报ValueError: check_hostname requires server_hostname

有说urllib3的bug ，发现solution都不完美， 所以暂时的workaround是关闭proxy 

参见：
 https://www.cnblogs.com/ceason/p/15222767.html快快看 
 
 https://www.its404.com/article/cjfkneoigoring/119487538
 
 https://blog.csdn.net/shizheng_Li/article/details/115838420
 
# 从豆瓣的反爬说说自建代理池
http://www.shenzhongqiang.com/douban-anticrawl-proxypool.html