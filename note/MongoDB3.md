

1. mongoDB find 返回指定字段 

返回匹配文档的所有字段:
如果没有指定projection，find()方法返回所有匹配文档的所有字段。
 
db.tbl_user.find({name:'lily'})
//这个例子将返回tbl_user集合中name字段的值为"lily"的所有文档，返回的文档包含全部字段。
 
返回指定字段和_id字段:
一个projection可以明确地指定多个字段。下面的操作中，find()方法返回匹配的所有文档。在结果集中，只有name和age字段，默认_id字段也是返回的。
 
db.tbl_user.find({name:'lily'}, {name:1,age:1} )
 
仅返回指定字段:
可以通过在projection中指定排除_id字段将其从结果中去掉，如下例子所示:
 
db.tbl_user.find({name:'lily'}, {name:1,age:1, _id:0 } )
 
返回除排除掉以外的字段:
可以使用一个projection排除一个或者一组字段，如下:
 
db.tbl_user.find({name:'lily'}, {name:0} )
//这个操作返回所有name字段值为lily的文档，在结果中name字段不返回。

2. 聚合管道


管道在Unix和Linux中一般用于将当前命令的输出结果作为下一个命令的参数。

MongoDB 的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。

表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。

聚合管道常用的几个操作：

$project：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。

$match：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。

$limit：用来限制MongoDB聚合管道返回的文档数。

$skip：在聚合管道中跳过指定数量的文档，并返回余下的文档。

$unwind：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。

$group：将集合中的文档分组，可用于统计结果。

$sort：将输入文档排序后输出。

$geoNear：输出接近某一地理位置的有序文档。





