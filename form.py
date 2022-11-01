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
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 51, 701))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CalendarButton.setIcon(icon1)
        self.CalendarButton.setIconSize(QtCore.QSize(999, 999))
        self.CalendarButton.setObjectName("CalendarButton")
        self.verticalLayout.addWidget(self.CalendarButton)
        self.TasksButton = QtWidgets.QPushButton(self.layoutWidget)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TasksButton.setIcon(icon2)
        self.TasksButton.setIconSize(QtCore.QSize(999, 999))
        self.TasksButton.setObjectName("TasksButton")
        self.verticalLayout.addWidget(self.TasksButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 0, 1201, 230))
        self.groupBox_2.setStyleSheet("color: #E6E697;")
        self.groupBox_2.setObjectName("groupBox_2")
        MainForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainForm", "Профиль"))