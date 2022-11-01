import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from form import Ui_CalendarButton as Form

class MyWidget(QMainWindow, Form):
    def __init__(self):
        self.flag = True
        super().__init__()
        self.setupUi(self)
        self.CalendarButton_2.clicked.connect(self.shide)

    def shide(self):
        if self.flag:
            self.HomeButton.hide()
        else:
            self.HomeButton.show()
        self.flag = not self.flag


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())