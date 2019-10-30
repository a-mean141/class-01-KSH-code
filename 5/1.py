import sys
from PyQt5.QtCore import Qt;
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLayout, QLineEdit, QToolButton;

class Calculator(QWidget):
    def __init__(self, parent=None):
      super().__init__(parent)

      self.display = QLineEdit('0')
      self.display.setReadOnly(True)
      self.display.setAlignment(Qt.AlignRight)
      self.display.setMaxLength(15)

      self.mainLayout = QGridLayout()
      self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
      self.mainLayout.addWidget(self.display, 0, 0, 1, 1)
      self.setWindowTitle('My Calculator')
      self.initNumberButtons()

      self.setLayout(self.mainLayout)

    def initNumberButtons(self):
      numbersLayout = QGridLayout()
      buttons = ['7', '8', '9', '*', '/', '4', '5', '6', '+', '-', '1', '2', '3', '(', ')', '0', '.', '=', 'c']
      for i in range(len(buttons)):
        button = QToolButton()
        button.setText(buttons[i])
        numbersLayout.addWidget(button, i / 5, i % 5)

      self.mainLayout.addLayout(numbersLayout, 1, 0)

app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
app.exec_()
