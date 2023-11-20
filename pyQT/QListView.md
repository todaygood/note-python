

获取QListView的所有item的文本

变量介绍

        【model】QListView对象

        【row_count】QListView对象的总行数

方法介绍

        model.index（行索引，列索引）

from PyQt5.QtCore import Qt
 
model = self.skuPreData.model()
row_count = self.skuPreData.model().rowCount()
for i in range(row_count):
    index = model.index(i, 0)  # 获取项目的索引
    text = model.data(index, Qt.DisplayRole)  # 获取项目的文本

————————————————
版权声明：本文为CSDN博主「gongzairen」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/gongzairen/article/details/130765286




https://zhuanlan.zhihu.com/p/638319835

