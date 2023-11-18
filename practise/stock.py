# coding=utf-8

import efinance as ef
import os
import time

class Share:
    code = ''
    name = '名称'
    zde = 1.0  # 涨跌额
    zdf = 0.01  # 涨跌幅度，百分比,如1%
    currentPrice = 1.0  # 当前价格
    yesClosePrice = 1.0  # 昨收
    openPrice = 1.0  # 今开
    high = 1.0  # 最高价
    low = 1.0  # 最低
    avg = 1.05  # 均价
    topPrice = 1.1  # 涨停价
    bottomPrice = 0.8  # 跌停价
    turnover = 0.1  # 换手率
    volume = 100  # 成交量
    amount = 10000  # 成交额

    def __init__(self, code):  # 初始化对象
        self.code = code
        try:
            ps = ef.stock.get_base_info(code)
            self.name = ps['股票名称']
        except Exception as e:
            print("获取{}信息失败:{}".format(code, e))

    def __str__(self):
        return "{} {}".format(
            self.name,
            self.code,
        )


class ShareMonitorInfo:
    def __init(self,share_monitor_info_dict):
        self.code = '002415'




