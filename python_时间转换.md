

## 从时间字符串转时间戳

 



[root@pcentos server]# grep 166847622  a.log  -irn    |grep 300850 
48447:2022-11-15 09:37:04,093 - DEBUG - enter warn_in_small_period 1668476224.0931673 code 300850
48451:2022-11-15 09:37:04,167 - DEBUG - enter warn_in_small_period 1668476224.167095 code 300850
48458:2022-11-15 09:37:04,716 - DEBUG - leave warn_in_small_period 1668476224.716483 code 300850
48470:2022-11-15 09:37:04,792 - DEBUG - leave warn_in_small_period 1668476224.7921243 code 300850




# 格式转换 - 转为 /
a2 = "2019/5/10 23:40:00"
# 先转换为时间数组,然后转换为其他格式
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
print(otherStyleTime)



