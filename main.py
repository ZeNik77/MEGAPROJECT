import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpacerItem, QSizePolicy, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFontDatabase, QFont
from form2 import Ui_MainForm as Form


class MyWidget(QMainWindow, Form):
    def __init__(self):
        QFontDatabase.addApplicationFont('font/regular.otf')
        super().__init__()
        self.setupUi(self)
        self.flag = {}
        self.tabs = [self.groupBox_2, self.groupBox_3, self.groupBox_4]
        for i in self.tabs:
            i.hide()
            self.flag[i] = False
        self.btns_init()
        self.fonts_init()

    def btns_init(self):
        self.btn_todo.clicked.connect(lambda: self.add_row(self.layout_todo, 1))
        self.btn_inprocess.clicked.connect(lambda: self.add_row(self.layout_inprocess, 2))
        self.btn_done.clicked.connect(lambda: self.add_row(self.layout_done, 3))
        self.AboutButton.clicked.connect(lambda: self.shide(self.groupBox_2))
        self.TasksButton.clicked.connect(lambda: self.shide(self.groupBox_3))
        self.CalendarButton.clicked.connect(lambda: self.shide(self.groupBox_4))
    def fonts_init(self):
        font_GB = QFont('Manrope', 24)
        self.font_labels = QFont('Manrope', 18)
        font_calendar = QFont('Manrope', 14)

        for el in self.arr_lbl:
            el.setFont(self.font_labels)
        for el in self.arr_calendar:
            el.setFont(font_calendar)
        for el in self.arr_GB:
            el.setFont(font_GB)
    def shide(self, GB):
        for i in self.tabs:
            i.hide()
        GB.show()

    def add_row(self, layout, type):
        self.clearSpacer(layout)
        le = QLineEdit(self)
        le.setFont(self.font_labels)
        lt = QHBoxLayout()
        if type == 1:
            btn_right = QPushButton(self)
            btn_right.setText('->')
            self.setStyleBtn(btn_right)
            btn_delete = QPushButton(self)
            btn_delete.setText('X')
            self.setStyleBtn(btn_delete)
            btn_right.setFont(self.font_labels)
            btn_delete.setFont(self.font_labels)
            lt.addWidget(le)
            lt.addWidget(btn_right)
            lt.addWidget(btn_delete)
        elif type == 2:
            btn_left = QPushButton(self)
            btn_left.setText('<-')
            self.setStyleBtn(btn_left)
            btn_delete = QPushButton(self)
            btn_delete.setText('X')
            self.setStyleBtn(btn_delete)
            btn_right = QPushButton(self)
            btn_right.setText('->')
            self.setStyleBtn(btn_right)
            btn_left.setFont(self.font_labels)
            btn_delete.setFont(self.font_labels)
            btn_right.setFont(self.font_labels)
            lt.addWidget(btn_left)
            lt.addWidget(le)
            lt.addWidget(btn_right)
            lt.addWidget(btn_delete)
        elif type == 3:
            btn_left = QPushButton(self)
            btn_left.setText('<-')
            self.setStyleBtn(btn_left)
            btn_delete = QPushButton(self)
            btn_delete.setText('X')
            self.setStyleBtn(btn_delete)
            btn_left.setFont(self.font_labels)
            btn_delete.setFont(self.font_labels)
            lt.addWidget(btn_left)
            lt.addWidget(le)
            lt.addWidget(btn_delete)
        layout.addLayout(lt)
        verticalSpacer = self.generate_spacer()
        layout.addItem(verticalSpacer)

    def setStyleBtn(self, button):
        button.setStyleSheet("QPushButton:hover\n"
                             "{\n"
                             " background-color: #2a0f66;\n"
                             "}\n"
                             "QPushButton\n"
                             "{\n"
                             "    background-color:#32127a;\n"
                             "    border-radius: 3;\n"
                             "}")

    def generate_spacer(self):
        return QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    def clearSpacer(self, layout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QSpacerItem):
                layout.removeItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
