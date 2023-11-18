

from iteration_utilities import unique_everseen

mylist = [{'股票代码': '601066', '股票名称': '中信建投'}, {'股票代码': '601066', '股票名称': '中信建投'}]

print(list(unique_everseen(mylist)))