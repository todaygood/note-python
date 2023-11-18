import sys
import os
import tushare as ts


# 获取年报的数据
df=ts.get_report_data(2021,4)
df.to_excel('年报数据-20220401.xlsx')


# 获取第一季度的数据
df=ts.get_report_data(2022,1)
df.to_excel('季报数据-20220401.xlsx')




'''

# 获取一季度预告数据

pro = ts.pro_api('0dfeea8ed14bc3484cbf73c60514033a0bdb8252d8ae29ce2169806d')
pro.forecast(ann_date='20220401', fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')
'''