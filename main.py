import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from form import Ui_MainForm as Form

class MyWidget(QMainWindow, Form):
    def __init__(self):
        QFontDatabase.addApplicationFont('font/regular.otf')
        super().__init__()
        self.setupUi(self)
        self.flag = {}
        self.groupBox_2.hide()
        self.flag[self.groupBox_2] = False
        self.AboutButton.clicked.connect(self.shide_GB2)
        font_GB = QFont('Manrope', 24)
        font_labels = QFont('Manrope', 18)
        self.groupBox_2.setFont(font_GB)
        self.label_name.setFont(font_labels)
        self.label_buttons.setFont(font_labels)
        self.label_devs.setFont(font_labels)
    
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