
import sys

# python 将输出信息写入文件中

mylog = open('recode.log', mode = 'a',encoding='utf-8')
for i in range(10):
    print("sdjlahjljag", file=mylog)
mylog.close()


