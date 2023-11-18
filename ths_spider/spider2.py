import requests
from urllib.parse import quote
from settings import *
from bs4 import BeautifulSoup
import sys
import time
import random
import csv
from copyheaders import headers_raw_to_dict
import pandas as pd

header1_string=b'''
Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Connection: keep-alive
Cookie: Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1650063033; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1650063033; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1650063033; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1650071272; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1650071272; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1650071272; v=A7fHVCOemdQmGB1YjTPHcsMpRqABfIvYZVAPUglk0wbtuNnaEUwbLnUgn6Aa
hexin-v: A7fHVCOemdQmGB1YjTPHcsMpRqABfIvYZVAPUglk0wbtuNnaEUwbLnUgn6Aa
Host: data.10jqka.com.cn
Referer: http://data.10jqka.com.cn/financial/yjyg/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
header2_string=b'''
Accept: text/html, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Connection: keep-alive
Cookie: Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1650112241; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1650112241; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1650112241; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1650112241; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1650112241; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1650112241; v=A-QVZVHwWg3Mka7BGA4k2zxYtenWfQmnyqCcNv4EcX1zL4pTJo3YdxqxbLhN
hexin-v: A-QVZVHwWg3Mka7BGA4k2zxYtenWfQmnyqCcNv4EcX1zL4pTJo3YdxqxbLhN
Host: data.10jqka.com.cn
Referer: http://data.10jqka.com.cn/financial/yjyg/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
X-Requested-With: XMLHttpRequest'''

headers_list = []
headers_list.append(headers_raw_to_dict(header1_string))
headers_list.append(headers_raw_to_dict(header2_string))

class crawl(object):

    def __init__(self):
        self.MAX_PAGE = MAX_PAGE
        self.PAGE_TRACK = PAGE_TRACK    #跟踪次数
        self.FLAG = FLAG                #设置标志位
        self.PAGE_LIST = PAGE_LIST      #第一次获取失败的 html 的 列表
        self.URL_START =  URL_START     #初始链接
        self.PARAMS = PARAMS            #url 构造参数
        #self.PROXY_POOL_API = "http://127.0.0.1:5555/random"
        self.PROXY_POOL_API = "http://127.0.0.1:5010/get"
        self.proxy_save = None   #用于存储代理
        self.proxy_con  = 0      #用于控制代理什么时候更换

    
    def proxy_get(self, num_retries=2):
        """
        #代理获取模块

        """
        try:
            #r_proxy = requests.get(self.PROXY_POOL_API, timeout = 5)
            #proxy = r_proxy.text  # 指定代理
            r_proxy_dict = requests.get(self.PROXY_POOL_API, timeout=5).json()
            proxy=r_proxy_dict.get("proxy")
            print("代理是", proxy)
            proxies = {
                "http": 'http://' + proxy,
                "https": 'https://' + proxy,
                }
            return proxies
        except:
            if num_retries > 0:
                print("代理获取失败，重新获取")
                self.proxy_get(num_retries-1)

   
    def url_yield(self):
        """
        :func 用于生成url
        :yield items
        """
        for i in range(1, self.MAX_PAGE + 1 ):
            self.PAGE_TRACK = i         #页面追踪
            self.FLAG += 1              #每次加1
            print('FLAG 是：', self.FLAG)
            url = "{}{}{}".format(self.URL_START, i, self.PARAMS) 
            yield url

    def url_omi(self):
        print("开始补漏")
        length_pl = len(self.PAGE_LIST) 
        if length_pl != 0:          #判断是否为空
            for i in range(length_pl):
                self.PAGE_TRACK = self.PAGE_LIST.pop(0)                  #构造一个动态列表, 弹出第一个元素
                url = "{}{}{}".format(self.URL_START, self.PAGE_TRACK, self.PARAMS) 
                yield url
    


    def downloader(self, url, num_retries=3):
        if self.proxy_con == 0:
            proxies = self.proxy_get()  #获取代理
        else:
            proxies = self.proxy_save   #继续使用代理
        self.proxy_save = proxies       #更换代理值


        try:
            time.sleep(random.random()*5)   #设置延时
            headers = random.choice(headers_list)
            r = requests.get(url, headers = headers, proxies=proxies, timeout=4)
        except:
            if num_retries > 0:
                print("重新下载")
                self.proxy_con = 0  #更换代理
                self.downloader(url,num_retries-1)
            else:
                if not self.PAGE_TRACK in self.PAGE_LIST:    #首先应该判断 该页是否存在列表中，如果不存在， 则将其加入其中
                        self.PAGE_LIST.append(self.PAGE_TRACK)   #将获取失败的url保存起来，后面再次循环利用，将元素添加在末尾，
        else:            
            return r.text


    def items_return(self):
        sys.setrecursionlimit(5000)
        count = 0
        df=pd.DataFrame()
        while True:
            if self.FLAG < self.MAX_PAGE:
                url_list = self.url_yield()   #获取url
            else:
                url_list = self.url_omi()
                if len(self.PAGE_LIST) ==0:
                    break
            print("执行到了获取模块")

            for url in url_list:
                html = self.downloader(url)
                #打印提示信息
                print('URL is:', url)
                items = {}   #建立一个空字典，用于信息存储
                try:
                    df = pd.concat([df, pd.read_html(html)[0]])
                    self.proxy_con = 1
                except:
                    print("解析失败")
                    #解析失败，则将代理换掉
                    self.proxy_con = 0
                    print(html)
                    if not self.PAGE_TRACK in self.PAGE_LIST:
                        self.PAGE_LIST.append(self.PAGE_TRACK)
                    else:
                        count += 1

            if count == 2:
                break

        df.to_excel('业绩.xlsx',index=False,encoding='utf-8')


if __name__ == '__main__':
    app = crawl()
    app.items_return()   #打印最后的结果



'''
 soup = BeautifulSoup(html, 'lxml')
                    for tr in soup.find('tbody').find_all('tr'):
                        td_list = tr.find_all('td')
                        items['代码'] = td_list[1].string
                        items['名称'] = td_list[2].string
                        items['现价'] = td_list[3].string
                        items['涨跌幅'] = td_list[4].string
                        self.writer.writerow(items)
                        print(items)
                        print("保存成功")
                        #如果保存成功，则继续使用代理
                        self.proxy_con = 1
                        #print("解析成功")
                        #yield items          #将结果返回
'''
