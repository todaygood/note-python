

## global 全局变量

在使用 global 关键字修饰变量名时，不能直接给变量赋初值，否则会引发语法错误。


## 分片 

分片用来从序列中提取出想要的子序列，其用法为：

var[lower:upper:step]

其范围包括 lower ，但不包括 upper ，即 [lower, upper)，
step 表示取值间隔大小，如果没有默认为1。

