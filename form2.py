# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1280, 720)
        MainForm.setStyleSheet("background-color: #0e0524;")
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -30, 71, 841))
        self.groupBox.setStyleSheet("background-color: #32127a;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"border-radius: 5px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 30, 71, 721))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HomeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.HomeButton.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.HomeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setIconSize(QtCore.QSize(999, 999))
        self.HomeButton.setObjectName("HomeButton")
        self.verticalLayout.addWidget(self.HomeButton)
        self.TasksButton = QtWidgets.QPushButton(self.layoutWidget)
        self.TasksButton.setEnabled(True)
        self.TasksButton.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.TasksButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TasksButton.setIcon(icon1)
        self.TasksButton.setIconSize(QtCore.QSize(999, 999))
        self.TasksButton.setObjectName("TasksButton")
        self.verticalLayout.addWidget(self.TasksButton)
        self.CalendarButton = QtWidgets.QPushButton(self.layoutWidget)
        self.CalendarButton.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.CalendarButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalendarButton.setIcon(icon2)
        self.CalendarButton.setIconSize(QtCore.QSize(999, 999))
        self.CalendarButton.setObjectName("CalendarButton")
        self.verticalLayout.addWidget(self.CalendarButton)
        self.AboutButton = QtWidgets.QPushButton(self.layoutWidget)
        self.AboutButton.setEnabled(True)
        self.AboutButton.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.AboutButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutButton.setIcon(icon3)
        self.AboutButton.setIconSize(QtCore.QSize(999, 999))
        self.AboutButton.setObjectName("AboutButton")
        self.verticalLayout.addWidget(self.AboutButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 480, 1201, 241))
        self.groupBox_2.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"border-radius: 5px;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 1101, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_name = QtWidgets.QLabel(self.layoutWidget1)
        self.label_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.label_buttons = QtWidgets.QLabel(self.layoutWidget1)
        self.label_buttons.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_buttons.setObjectName("label_buttons")
        self.verticalLayout_2.addWidget(self.label_buttons)
        self.label_devs = QtWidgets.QLabel(self.layoutWidget1)
        self.label_devs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_devs.setObjectName("label_devs")
        self.verticalLayout_2.addWidget(self.label_devs)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 0, 1211, 721))
        self.groupBox_3.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"border-radius: 5px;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 1181, 661))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_inprocess = QtWidgets.QVBoxLayout()
        self.layout_inprocess.setObjectName("layout_inprocess")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_left1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_left1.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_left1.setObjectName("btn_left1")
        self.horizontalLayout_3.addWidget(self.btn_left1)
        self.lineEdit_st2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_st2.setObjectName("lineEdit_st2")
        self.horizontalLayout_3.addWidget(self.lineEdit_st2)
        self.btn_right2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_right2.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_right2.setObjectName("btn_right2")
        self.horizontalLayout_3.addWidget(self.btn_right2)
        self.btn_delete2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_delete2.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_delete2.setObjectName("btn_delete2")
        self.horizontalLayout_3.addWidget(self.btn_delete2)
        self.layout_inprocess.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_inprocess.addItem(spacerItem)
        self.gridLayout.addLayout(self.layout_inprocess, 3, 2, 1, 1)
        self.layout_todo = QtWidgets.QVBoxLayout()
        self.layout_todo.setObjectName("layout_todo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_st1 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_st1.setObjectName("lineEdit_st1")
        self.horizontalLayout_2.addWidget(self.lineEdit_st1)
        self.btn_right1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_right1.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_right1.setObjectName("btn_right1")
        self.horizontalLayout_2.addWidget(self.btn_right1)
        self.btn_delete1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_delete1.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_delete1.setObjectName("btn_delete1")
        self.horizontalLayout_2.addWidget(self.btn_delete1)
        self.layout_todo.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_todo.addItem(spacerItem1)
        self.gridLayout.addLayout(self.layout_todo, 3, 0, 1, 1)
        self.layout_done = QtWidgets.QVBoxLayout()
        self.layout_done.setObjectName("layout_done")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_left2 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_left2.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_left2.setObjectName("btn_left2")
        self.horizontalLayout_4.addWidget(self.btn_left2)
        self.lineEdit_st3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_st3.setObjectName("lineEdit_st3")
        self.horizontalLayout_4.addWidget(self.lineEdit_st3)
        self.btn_delete3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_delete3.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_delete3.setObjectName("btn_delete3")
        self.horizontalLayout_4.addWidget(self.btn_delete3)
        self.layout_done.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_done.addItem(spacerItem2)
        self.gridLayout.addLayout(self.layout_done, 3, 3, 1, 1)
        self.btn_inprocess = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_inprocess.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_inprocess.setObjectName("btn_inprocess")
        self.gridLayout.addWidget(self.btn_inprocess, 1, 2, 1, 1)
        self.btn_done = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_done.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_done.setObjectName("btn_done")
        self.gridLayout.addWidget(self.btn_done, 1, 3, 1, 1)
        self.label_inprocess = QtWidgets.QLabel(self.layoutWidget2)
        self.label_inprocess.setObjectName("label_inprocess")
        self.gridLayout.addWidget(self.label_inprocess, 0, 2, 1, 1)
        self.label_todo = QtWidgets.QLabel(self.layoutWidget2)
        self.label_todo.setObjectName("label_todo")
        self.gridLayout.addWidget(self.label_todo, 0, 0, 1, 1)
        self.btn_todo = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_todo.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_todo.setObjectName("btn_todo")
        self.gridLayout.addWidget(self.btn_todo, 1, 0, 1, 1)
        self.label_done = QtWidgets.QLabel(self.layoutWidget2)
        self.label_done.setObjectName("label_done")
        self.gridLayout.addWidget(self.label_done, 0, 3, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(70, 0, 1211, 721))
        self.groupBox_4.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"border-radius: 5px;")
        self.groupBox_4.setObjectName("groupBox_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_4)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 50, 1131, 631))
        self.calendarWidget.setObjectName("calendarWidget")
        MainForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainForm", "О приложении"))
        self.label_name.setText(_translate("MainForm", "Многофункциональный органайзер"))
        self.label_buttons.setText(_translate("MainForm", "Кнопки: Home, расписание / задачник, календарь, помощь"))
        self.label_devs.setText(_translate("MainForm", "Разработчики: Зеленов Никита и Веретенов Арсений"))
        self.groupBox_3.setTitle(_translate("MainForm", "Расписание"))
        self.btn_left1.setText(_translate("MainForm", "<-"))
        self.btn_right2.setText(_translate("MainForm", "->"))
        self.btn_delete2.setText(_translate("MainForm", "X"))
        self.btn_right1.setText(_translate("MainForm", "->"))
        self.btn_delete1.setText(_translate("MainForm", "X"))
        self.btn_left2.setText(_translate("MainForm", "<-"))
        self.btn_delete3.setText(_translate("MainForm", "X"))
        self.btn_inprocess.setText(_translate("MainForm", "Добавить..."))
        self.btn_done.setText(_translate("MainForm", "Добавить..."))
        self.label_inprocess.setText(_translate("MainForm", "В процессе"))
        self.label_todo.setText(_translate("MainForm", "Сделать"))
        self.btn_todo.setText(_translate("MainForm", "Добавить..."))
        self.label_done.setText(_translate("MainForm", "Готово"))
        self.groupBox_4.setTitle(_translate("MainForm", "Календарь"))
