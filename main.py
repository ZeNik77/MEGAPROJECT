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
        self.AboutButton.clicked.connect(self.shide_GB2)
        self.TasksButton.clicked.connect(self.shide_GB3)
        self.CalendarButton.clicked.connect(self.shide_GB4)
        font_GB = QFont('Manrope', 24)
        self.font_labels = QFont('Manrope', 18)
        font_calendar = QFont('Manrope', 14)
        self.groupBox_2.setFont(font_GB)
        self.label_name.setFont(self.font_labels)
        self.label_buttons.setFont(self.font_labels)
        self.label_devs.setFont(self.font_labels)
        self.btn_todo.setFont(self.font_labels)
        self.btn_inprocess.setFont(self.font_labels)
        self.btn_done.setFont(self.font_labels)
        
        self.groupBox_3.setFont(font_GB)
        self.label_todo.setFont(self.font_labels)
        self.label_inprocess.setFont(self.font_labels)
        self.label_done.setFont(self.font_labels)
        self.lineEdit_st1.setFont(self.font_labels)
        self.lineEdit_st2.setFont(self.font_labels)
        self.lineEdit_st3.setFont(self.font_labels)

        self.groupBox_4.setFont(font_GB)
        self.label_week.setFont(font_calendar)
        self.label_Monday.setFont(font_calendar)
        self.label_Tuesday.setFont(font_calendar)
        self.label_Wednesday.setFont(font_calendar)
        self.label_Thursday.setFont(font_calendar)
        self.label_Friday.setFont(font_calendar)
        self.label_Saturday.setFont(font_calendar)
        self.label_Sunday.setFont(font_calendar)
        self.label_w1.setFont(font_calendar)
        self.label_w2.setFont(font_calendar)
        self.label_w3.setFont(font_calendar)
        self.label_w4.setFont(font_calendar)
        self.label_w5.setFont(font_calendar)

        self.btn_todo.clicked.connect(self.add_todo)
        self.btn_inprocess.clicked.connect(self.add_inprocess)
        self.btn_done.clicked.connect(self.add_done)


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
    def shide_GB4(self):
        if self.flag[self.groupBox_4]:
            self.groupBox_4.hide()
        else:
            self.groupBox_4.show()
        self.flag[self.groupBox_4] = not self.flag[self.groupBox_4]

    def add_todo(self, layout):
        self.clearSpacer(self.layout_todo)
        le = QLineEdit(self)
        le.setFont(self.font_labels)
        self.layout_todo.addWidget(le)
        verticalSpacer = self.generate_spacer()
        self.layout_todo.addItem(verticalSpacer)

    def add_inprocess(self, layout):
        self.clearSpacer(self.layout_inprocess)
        le = QLineEdit(self)
        le.setFont(self.font_labels)
        self.layout_inprocess.addWidget(le)
        verticalSpacer = self.generate_spacer()
        self.layout_inprocess.addItem(verticalSpacer)

    def add_done(self, layout):
        self.clearSpacer(self.layout_done)
        le = QLineEdit(self)
        le.setFont(self.font_labels)
        self.layout_done.addWidget(le)
        verticalSpacer = self.generate_spacer()
        self.layout_done.addItem(verticalSpacer)

    def generate_spacer(self):
        return QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)


    def clearSpacer(self, layout):
        if layout is not None:
            for i in range(layout.count()):
                item = layout.itemAt(i)
                if isinstance(item, QSpacerItem):
                    layout.removeItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())