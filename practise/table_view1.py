import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout,QAbstractItemView

my_array = [['00', '01', '02'],
            ['10', '11', '12'],
            ['20', '21', '22']]


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())


class MyWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)

        tablemodel = MyTableModel(my_array, self)
        tableview = QTableView()
        tableview.setModel(tablemodel)

        tableview.verticalHeader().hide()
        tableview.horizontalHeader().hide()
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableview.setEditTriggers(QAbstractItemView.DoubleClicked)
        tableview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        tableview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        """
        layout = QVBoxLayout(self)
        layout.addWidget(tableview)
        self.setLayout(layout)
        """
        self.setCentralWidget(tableview)
        self.setGeometry(0, 0, 500, 600)


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.arraydata[index.row()][index.column()]

    def setData(self, index, value):
        self.arraydata[index.row()][index.column()] = value
        return True

    def flags(self, index):
        return  Qt.ItemIsEditable |  Qt.ItemIsEnabled |  Qt.ItemIsSelectable


if __name__ == "__main__":
    main()
