from datetime import datetime
from chinese_calendar import is_workday



"""
# 获取最新一个公开的龙虎榜数据(后面还有获取指定日期区间的示例代码)
today= datetime.today().strftime('%Y-%m-%d')
print(today)

hour= int(datetime.now().strftime('%H'))
"""
today=datetime.today()

a=is_workday(today)
print(a)

