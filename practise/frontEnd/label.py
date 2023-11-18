# Only needed for access to command line arguments
import sys
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow,QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        self.label.setText("mousePress")



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = QWidget()

window = MainWindow()

# window = QPushButton("Push Me")
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
