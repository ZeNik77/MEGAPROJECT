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
        self.groupBox_3.hide()
        self.flag[self.groupBox_2] = False
        self.flag[self.groupBox_3] = False
        self.AboutButton.clicked.connect(self.shide_GB2)
        self.TasksButton.clicked.connect(self.shide_GB3)
        font_GB = QFont('Manrope', 24)
        font_labels = QFont('Manrope', 18)
        self.groupBox_2.setFont(font_GB)
        self.label_name.setFont(font_labels)
        self.label_buttons.setFont(font_labels)
        self.label_devs.setFont(font_labels)
        self.btn_todo.setFont(font_labels)
        self.btn_inprocess.setFont(font_labels)
        self.btn_done.setFont(font_labels)
        self.groupBox_3.setFont(font_GB)
        self.label_todo.setFont(font_labels)
        self.label_inprocess.setFont(font_labels)
        self.label_done.setFont(font_labels)
    
    def shide_GB2(self):
        if self.flag[self.groupBox_2]:
            self.groupBox_2.hide()
        else:
            self.groupBox_2.show()
        self.flag[self.groupBox_2] = not self.flag[self.groupBox_2]
    def shide_GB3(self):
        if self.flag[self.groupBox_3]:
            self.groupBox_3.hide()
        else:
            self.groupBox_3.show()
        self.flag[self.groupBox_3] = not self.flag[self.groupBox_3]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())