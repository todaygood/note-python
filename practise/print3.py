


stock_list=[{'股票代码': '002606', '股票名称': '大连电瓷'}, {'股票代码': '601700', '股票名称': '风范股份'}, {'股票代码': '601179', '股票名称': '中国西电'}, {'股票代码': '600312', '股票名称': '平高电气'}, {'股票代码': '600268', '股票名称': '国电南自'}, {'股票代码': '300510', '股票名称': '金冠股份'}, {'股票代码': '300617', '股票名称': '安靠智电'}, {'股票代码': '300215', '股票名称': '电科院'}, {'股票代码': '601126', '股票名称': '四方股份'}]

def print_stock_list(stock_list):
    a=""
    for one in stock_list:
        a += "{}{},".format(one['股票名称'],one['股票代码'])

    b=a.rstrip(',')
    return b


print(print_stock_list(stock_list))

for k,v in enumerate(stock_list):
    print(k,v)