import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("SWP2")
    self.setGeometry(300, 300, 300, 400)

app = QApplication(sys.argv)
my_window = MyWindow()
my_window.show()
app.exec_()
