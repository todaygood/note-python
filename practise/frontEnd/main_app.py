"""
https://zhuanlan.zhihu.com/p/269273821

pyuic6  -o main_ui.py main.ui

pushButton就是刚刚获取的按钮id
clicked就是信号，因为是点击，所以我们这里用clicked
click_success就是对应要调用的槽，注意这里函数并不写成click_success()


"""

import sys
import main_ui
from PyQt6.QtWidgets import QApplication, QMainWindow




def click_success():
    print("使用Qt Designer成功了")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(click_success)
    app.exec()
