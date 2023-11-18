import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 35px')
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        linkTemplate = '<a href={0}>{1}</a>'

        label1 = HyperlinkLabel(self)
        label1.setText(linkTemplate.format('http://quote.eastmoney.com/zixuan/lite.html', '东方财富自选股'))

        label2 = HyperlinkLabel(self)
        label2.setText(linkTemplate.format('http://quote.eastmoney.com/concept/sh600233.html#fschart-r', '看K线'))
        label2.move(0, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec())
