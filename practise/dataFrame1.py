
from pandas.core.frame import DataFrame

# Pandas将列表（List）转换为数据框（Dataframe）

a=[[1,2,3,4],[5,6,7,8]]      #包含两个不同的子列表[1,2,3,4]和[5,6,7,8]
data=DataFrame(a)            #这时候是以行为标准写入的

print(data)



a=[1,2,3,4]   #列表a
b=[5,6,7,8]   #列表b

c={"a" : a, "b" : b}      #将列表a，b转换成字典
data=DataFrame(c)         #将字典转换成为数据框

print(data)
