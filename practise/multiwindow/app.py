import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import win1
import win2


def show_new_window():
    secondWin = QMainWindow()
    w = win2.Ui_MainWindow(secondWin)
    w.setupUi()
    w.show()



app = QApplication(sys.argv)
MainWindow = QMainWindow()

ui = win1.Ui_MainWindow()

ui.setupUi(MainWindow)   # 构建界面的各个元素

ui.pushButton.clicked.connect(show_new_window)
MainWindow.show()


app.exec()