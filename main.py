import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QSpacerItem, QSizePolicy
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
        self.groupBox_4.hide()
        self.flag[self.groupBox_2] = False
        self.flag[self.groupBox_3] = False
        self.flag[self.groupBox_4] = False
        self.AboutButton.clicked.connect(lambda: self.shide(self.groupBox_2))
        self.TasksButton.clicked.connect(lambda: self.shide(self.groupBox_3))
        self.CalendarButton.clicked.connect(lambda: self.shide(self.groupBox_4))

        font_GB = QFont('Manrope', 24)
        self.font_labels = QFont('Manrope', 18)
        font_calendar = QFont('Manrope', 14)
        arr_lbl = [self.label_name, self.label_buttons, self.label_devs, self.btn_todo, self.btn_inprocess, self.btn_done, self.label_todo, self.label_inprocess, self.label_done, self.lineEdit_st1, self.lineEdit_st2, self.lineEdit_st3]
        arr_calendar = [self.label_week, self.label_Monday, self.label_Tuesday, self.label_Wednesday, self.label_Thursday, self.label_Friday, self.label_Saturday, self.label_Sunday, self.label_w1, self.label_w2, self.label_w3, self.label_w4, self.label_w5]
        arr_GB = [self.groupBox_2, self.groupBox_3, self.groupBox_4]
        for el in arr_lbl:
            el.setFont(self.font_labels)
        for el in arr_calendar:
            el.setFont(font_calendar)
        for el in arr_GB:
            el.setFont(font_GB)

        self.btn_todo.clicked.connect(lambda: self.add_row(self.layout_todo))
        self.btn_inprocess.clicked.connect(lambda: self.add_row(self.layout_inprocess))
        self.btn_done.clicked.connect(lambda: self.add_row(self.layout_done))


    def shide(self, GB):
        if self.flag[GB]:
            GB.hide()
        else:
            GB.show()
        self.flag[GB] = not self.flag[GB]

    def add_row(self, layout):
        self.clearSpacer(layout)
        le = QLineEdit(self)
        le.setFont(self.font_labels)
        layout.addWidget(le)
        verticalSpacer = self.generate_spacer()
        layout.addItem(verticalSpacer)


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