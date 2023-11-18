


https://zhuanlan.zhihu.com/p/388088384

系列文章:
https://www.zhihu.com/people/la-ge-lang-ri-96-69

股票龙虎榜（指定日期区间的数据）
# 导入 efinance 库
import efinance as ef
# 指定日期区间的龙虎榜数据
df = ef.stock.get_daily_billboard(start_date='2021-09-01',end_date='2021-09-10')
df


# 使用python做一个盯盘机器人
  程序首先下载股票上一个交易日之前的日K线行情数据，然后计算上一交易日的20日均线，然后比较上一交易日20日均线的值和过去10天最高收盘价两个值，取其中的最大值作为阻力线，然后再获取当日实时数据，如果某个时刻突破了这个阻力线，则发出提示信息。这只是个简单的策略，大家可以自己在我的程序基础上，设定自己的策略。
  
  https://www.codeleading.com/article/90332757643/
  
  
  
https://pythonmana.com/2021/12/202112201626290466.html


发邮件 参见 https://developer.51cto.com/article/678518.html

