# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(325, 243)
        Form.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: #0e0524;")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 26, 311, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_name.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"bord")
        self.le_name.setObjectName("le_name")
        self.verticalLayout.addWidget(self.le_name)
        self.le_desc = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_desc.setStyleSheet("color: #E6E697;\n"
"border: 2px solid gray;\n"
"padding: 10px;\n"
"bord")
        self.le_desc.setObjectName("le_desc")
        self.verticalLayout.addWidget(self.le_desc)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.btn_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_ok.setStyleSheet("QPushButton:hover\n"
"{\n"
" background-color: #2a0f66;\n"
"}\n"
"QPushButton\n"
"{\n"
"    background-color:#32127a;\n"
"    border-radius: 3;\n"
"}")
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.le_name.setText(_translate("Form", "Название"))
        self.le_desc.setText(_translate("Form", "Описание"))
        self.btn_ok.setText(_translate("Form", "Ок"))
