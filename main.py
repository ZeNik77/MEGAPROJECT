import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QCheckBox, QTimeEdit, QWidgetItem
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QTime, QDateTime
from form2 import Ui_MainForm as Form
from create_form import Ui_Form
import sqlite3

class Window2(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.setupUi(self)


class MyWidget(QMainWindow, Form):
    def __init__(self):
        QFontDatabase.addApplicationFont('Assets/font/regular.otf')
        super().__init__()
        self.setupUi(self)
        # self.flag = {}
        self.tabs = [self.groupBox_2, self.groupBox_3, self.groupBox_4, self.groupBox_5]
        for i in self.tabs:
            i.hide()
            # self.flag[i] = False
        self.ex = Window2(self)
        self.btns_init()
        self.fonts_init()
    def btns_init(self):
        self.btn_todo.clicked.connect(lambda: self.add_row(self.layout_todo, 1))
        self.btn_inprocess.clicked.connect(lambda: self.add_row(self.layout_inprocess, 2))
        self.btn_done.clicked.connect(lambda: self.add_row(self.layout_done, 3))
        self.AboutButton.clicked.connect(lambda: self.shide(self.groupBox_2))
        self.TasksButton.clicked.connect(lambda: self.shide(self.groupBox_3))
        self.CalendarButton.clicked.connect(lambda: self.shide(self.groupBox_4))
        self.btn_closeGB5.clicked.connect(self.hide_GB5)
        self.calendarWidget.clicked.connect(self.get_date)
        self.btn_add_event.clicked.connect(lambda: self.ex.show())
        self.ex.btn_ok.clicked.connect(lambda: self.add_event(self.ex.le_name.text(), self.ex.le_desc.text(), self.clicked_year, self.clicked_month, self.clicked_day, self.ex.timeEdit.time().hour(), self.ex.timeEdit.time().minute()))
    def fonts_init(self):
        font_GB = QFont('Manrope', 24)
        self.font_labels = QFont('Manrope', 18)
        font_calendar = QFont('Manrope', 14)
        arr_lbl = [self.label_name, self.label_buttons, self.label_devs, self.btn_todo, self.btn_inprocess,
                   self.btn_done, self.label_todo, self.label_inprocess, self.label_done, self.lineEdit_st1,
                   self.lineEdit_st2, self.lineEdit_st3, self.btn_right1, self.btn_delete1, self.btn_left1,
                   self.btn_right2, self.btn_delete2, self.btn_left2, self.btn_delete3, self.btn_closeGB5, self.btn_add_event]
        # self.arr_calendar = [self.label_week, self.label_Monday, self.label_Tuesday, self.label_Wednesday,
        #                 self.label_Thursday, self.label_Friday, self.label_Saturday, self.label_Sunday, self.label_w1,
        #                 self.label_w2, self.label_w3, self.label_w4, self.label_w5]
        for el in self.tabs:
            el.setFont(font_GB)
        for el in arr_lbl:
            el.setFont(self.font_labels)
        self.calendarWidget.setFont(font_calendar)


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
    
    def clearLayout(self, layout):
        layouts = []
        for i in range(layout.count()):
            if (type(layout.itemAt(i)) == QVBoxLayout):
                self.clearLayout(layout.itemAt(i))
                layouts.append(layout.itemAt(i))
            else:
                if (type(layout.itemAt(i)) == QWidgetItem):
                    layout.itemAt(i).widget().close()

    def get_date(self):
        self.clearLayout(self.layout_events)
        self.clicked_year = self.calendarWidget.selectedDate().year()
        self.clicked_month = self.calendarWidget.selectedDate().month()
        self.clicked_day = self.calendarWidget.selectedDate().day()
        self.groupBox_5.setTitle(f'Мероприятия на {self.clicked_day}.{self.clicked_month}.{self.clicked_year}:')
        con = sqlite3.connect('Assets/Databases/main.sqlite3')
        cur = con.cursor()
        events = cur.execute(f"SELECT * FROM EVENTS WHERE YEAR = {self.clicked_year} AND  MONTH = {self.clicked_month} AND DAY = {self.clicked_day}").fetchall()
        font = QFont('Manrope', 14)
        label_name = []
        label_desc = []
        label_time = []
        te = []
        cb = []
        btn_delete = []
        id = []
        name = []
        desc = []
        hour = []
        minute = []
        done = []
        layouts = []

        for i in range(len(events)):
            layouts.append(QVBoxLayout())
            id.append(events[i][0])
            name.append(events[i][1])
            desc.append(events[i][2])
            hour.append(events[i][6])
            minute.append(events[i][7])
            done.append(events[i][8])
            label_name.append(QLabel())
            label_name[i].setFont(QFont('Manrope', 24))
            label_name[i].setText(name[i])

            label_desc.append(QLabel())
            label_desc[i].setFont(font)
            label_desc[i].setText(desc[i])

            label_time.append(QLabel())
            label_time[i].setText('Дедлайн:')
            label_time[i].setFont(font)

            te.append(QTimeEdit())
            te[i].setFont(font)
            te[i].setTime(QTime(hour[i], minute[i], 00))

            cb.append(QCheckBox())

            btn_delete.append(QPushButton())
            btn_delete[i].setFont(font)
            btn_delete[i].setText('Удалить мероприятие')
            self.setStyleBtn(btn_delete[i])
            btn_delete[i].clicked.connect(lambda x, b=int(id[i]): self.delete_event(b))
            layouts[i].addWidget(label_name[i])
            layouts[i].addWidget(label_desc[i])
            layouts[i].addWidget(label_time[i])
            layouts[i].addWidget(te[i])
            layouts[i].addWidget(cb[i])
            layouts[i].addWidget(btn_delete[i])
            self.layout_events.addLayout(layouts[i])
        self.groupBox_5.show()
    
    def add_event(self, name, desc, year, month, day, hour, minute):
        con = sqlite3.connect('Assets/Databases/main.sqlite3')
        cur = con.cursor()
        id = cur.execute("SELECT * FROM EVENTS").fetchall()[-1][0] + 1
        cur.execute(f"INSERT INTO EVENTS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, name, desc, year, month, day, hour, minute, 0))
        con.commit()
        con.close()
        self.ex.le_name.clear()
        self.ex.le_desc.clear()
        self.ex.hide()
        self.get_date()
    
    def delete_event(self, id):
        con = sqlite3.connect('Assets/Databases/main.sqlite3')
        cur = con.cursor()
        cur.execute("DELETE FROM EVENTS WHERE ID = ?", (id,))
        con.commit()
        con.close()
        self.get_date()

    def hide_GB5(self):
        self.clearLayout(self.layout_events)
        self.groupBox_5.hide()

    def show_window2(self):
        self.ex.timeEdit.setDateTime(QDateTime(self.clicked_year, self.clicked_month, self.clicked_day))
        self.ex.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
