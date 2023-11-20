
## QURL

## QLineEdit 

设置只读了之后，修改它的text 就会报错。

## import

头文件包含，用这个

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

就足够了。


## QListWidget

QlistView类用于展示数据，它的子类是QListWIdget。QListView是基于模型（Model）的，需要程序来建立模型，然后再保存数据
QListWidget是一个升级版本的QListView，它已经建立了一个数据储存模型（QListWidgetItem），直接调用addItem（）函数，就可以添加条目（Item）
————————————————
版权声明：本文为CSDN博主「jia666666」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/jia666666/article/details/81624550


## QT 程序调试方法

https://blog.csdn.net/mao_hui_fei/article/details/117289614






## TableView 

知识点： https://blog.csdn.net/qq_44826637/article/details/114582026 

https://zhuanlan.zhihu.com/p/442963552  重定义Model 

QStandardItemModel：可以作为QListView、QTableView、QTreeView的标准model。

QAbstractListModel：需要使用QListView显示数据，并配合自定义model时，我们从此类继承。
QAbstractTableModel：需要使用QTableView显示数据时，并配合自定义model时，我们从此类继承。
QAbstractItemModel：需要使用QTreeView显示数据时，并配合自定义model时，我们从此类继承。

获取表格数据
self.table_view.currentIndex().row() # 获取所在行数
self.table_view.currentIndex().column()  # 获取所在列数

获得单元格的内容
self.table_view.currentIndex().data()

原文链接：https://blog.csdn.net/qq_38416013/article/details/114449385


数据的显示、编辑、删除与添加也是GUI编程的常见功能，作为初用者，使用笨拙的方式基本实现的功能。运用QTableView和QStandardItemModel相结合的方式实现数据的显示与增、删、改。
了解了PyQt5的Model/View/Delegate的设计模式，即Model持有数据，下与数据源交互（数据的查询、修改与添加），上与View交互，主要为View提供要显示的数据。View提供数据的显示和与用户交互。Delegate可以实现定制数据显示的方式和编辑方式，在实际使用时，Delegate可以不用自定义，而使用默认的实现即可。实现简单的功能，只通过继承PyQt5.QtCore.QAbstractTableModel能更方便的实现数据的CRUD，但是需要了解必须实现的接口方法及其功能。以下是通过继承PyQt5.QtCore.QAbstractTableModel自定义自定义一个Model的实例代码。

https://www.cxyzjd.com/article/cloveses/80943496

[该怎么用pyqt5来实现数据的增、删、改、查功能](https://zhuanlan.zhihu.com/p/482754031)


判断tableview 中选择的行数：https://stackoverflow.com/questions/22577327/how-to-retrieve-the-selected-row-of-a-qtableview

indexes = table.selectionModel().selectedRows()
    for index in sorted(indexes):
        print('Row %d is selected' % index.row())




## pyQt5 信号与槽

PyQt5快速入门（二）PyQt5信号槽机制 https://blog.51cto.com/quantfabric/2422187


















## bug 

Traceback (most recent call last):
  File "urllib3\connectionpool.py", line 703, in urlopen
  File "urllib3\connectionpool.py", line 386, in _make_request
  File "urllib3\connectionpool.py", line 1040, in _validate_conn
  File "urllib3\connection.py", line 414, in connect
  File "urllib3\util\ssl_.py", line 449, in ssl_wrap_socket
  File "urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl
  File "ssl.py", line 500, in wrap_socket
  File "ssl.py", line 1040, in _create
  File "ssl.py", line 1309, in do_handshake
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:1131)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "requests\adapters.py", line 440, in send
  File "urllib3\connectionpool.py", line 785, in urlopen
  File "urllib3\util\retry.py", line 592, in increment
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='mp.weixin.qq.com', port=443): Max retries exceeded with url: /cgi-bin/appmsg?token=1604983175&lang=zh_CN&f=json&ajax=1&action=list_ex&begin=0&count=5&query=&fakeid=MzUxMzAzMzk5Ng%3D%3D&type=9 (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1131)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "down_articles_to_db.py", line 532, in <module>
  File "down_articles_to_db.py", line 356, in store_one_onepage_articles_to_db
  File "down_articles_to_db.py", line 182, in get_wx_gzh_one_page_articles
  File "requests\api.py", line 75, in get
  File "requests\api.py", line 61, in request
  File "requests\sessions.py", line 529, in request
  File "requests\sessions.py", line 645, in send
  File "requests\adapters.py", line 517, in send
requests.exceptions.SSLError: HTTPSConnectionPool(host='mp.weixin.qq.com', port=443): Max retries exceeded with url: /cgi-bin/appmsg?token=1604983175&lang=zh_CN&f=json&ajax=1&action=list_ex&begin=0&count=5&query=&fakeid=MzUxMzAzMzk5Ng%3D%3D&type=9 (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1131)')))


