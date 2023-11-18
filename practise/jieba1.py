import jieba



strs=["【快讯：农业板块震荡走强 万向德农涨停】财联社5月9日电，万向德农涨停，美晨生态、农发种业、万辰生物、荃银高科、华绿生物、雪榕生物、登海种业、神农科技等跟涨。"]

for str in strs:
    seg_list= jieba.cut(str)
    print("default Mode: " +"/ ".join(list(seg_list)))

#seg_list= jieba.cut("我来到北京清华大学",cut_all=True)
#print("Full Mode: " + "/ ".join(seg_list))