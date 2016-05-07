# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/query.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.label_po = QtWidgets.QLabel(Form)
        self.label_po.setGeometry(QtCore.QRect(40, 30, 101, 41))
        self.label_po.setObjectName("label_po")
        self.lineEdit_po = QtWidgets.QLineEdit(Form)
        self.lineEdit_po.setGeometry(QtCore.QRect(150, 40, 141, 27))
        self.lineEdit_po.setObjectName("lineEdit_po")
        self.button_po = QtWidgets.QPushButton(Form)
        self.button_po.setGeometry(QtCore.QRect(308, 40, 71, 27))
        self.button_po.setObjectName("button_po")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MAC查询"))
        self.label_po.setText(_translate("Form", "请输入订单号"))
        self.button_po.setText(_translate("Form", "查询"))

