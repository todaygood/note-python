

import pandas as pd

df = pd.DataFrame()


for i in range(1, 26):
    url = f'http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jjzc/index.phtml?p={i}'

    df = pd.concat([df, pd.read_html(url)[0].iloc[::,:-1]])    # 合并DataFrame  不要明细那一列




df.to_excel('新浪财经基金重仓股数据.xlsx',encoding='utf-8')


