import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from form import Ui_MainForm as Form

class MyWidget(QMainWindow, Form):
    def __init__(self):
        QFontDatabase.addApplicationFont('font/regular.otf')

        
        self.flag = True
        super().__init__()
        self.setupUi(self)
        self.flag = {}
        self.flag[self.groupBox_2] = True
        self.flag[self.HomeButton] = True
        self.HomeButton.clicked.connect(self.shide_GB2)
        font = QFont('Manrope', 24)
        self.groupBox_2.setFont(font)
    
    def shide_GB2(self):
        if self.flag[self.groupBox_2]:
            self.groupBox_2.hide()
        else:
            self.groupBox_2.show()
        self.flag[self.groupBox_2] = not self.flag[self.groupBox_2]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())