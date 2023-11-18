
import pandas as pd

dates = pd.date_range('20190101', '20191201', freq='MS').strftime('%Y%m')   # 构造出日期序列  便于之后构造url
print(dates)


for i in range(len(dates)):
    # print("i={a}".format(a=i))
    df = pd.read_html(f'http://www.tianqihoubao.com/aqi/chengdu-{dates[i]}.html', encoding='gbk', header=0)[0]
    if i == 0:
        df.to_csv('2019年成都空气质量数据.csv', mode='a+', index=False)     # 追加写入
    else:
        df.to_csv('2019年成都空气质量数据.csv', mode='a+', index=False, header=False)



