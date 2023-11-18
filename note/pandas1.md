

# 构造一个空的dataframe
import pandas as pd
df = pd.DataFrame(columns=['name','number'])
# 采用.loc的方法进行
df.loc[0]=['cat', 3]  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
df.loc[1]=['abt',4]
print(df)
# 也可采用诸如df.loc['a'] = ['123',30]的形式

df.insert(1, 'tail', [1,4], allow_duplicates=False)
print(df)




