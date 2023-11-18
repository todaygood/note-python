# Only needed for access to command line arguments
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("鹰之眼")
        self.button_is_checked = True

        button = QPushButton("看K线")
        button.setCheckable(True)

        # button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)
        button.released.connect(self.the_button_was_released)
        button.setChecked(self.button_is_checked)

        button.setFixedSize(QSize(50,30))

        self.button = button
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self,checked):
        print("checked?",checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print("released?",self.button_is_checked)



app = QApplication(sys.argv)
window = MainWindow()


window.show()

# Start the event loop.
app.exec()
