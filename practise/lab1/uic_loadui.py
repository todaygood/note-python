import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic



app = QApplication(sys.argv)
window = uic.loadUi("MainWindow.ui")

window.show()

app.exec()
