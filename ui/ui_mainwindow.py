# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 130, 218, 42))
        self.layoutWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(36)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_cur = QtWidgets.QLabel(self.layoutWidget)
        self.label_cur.setMinimumSize(QtCore.QSize(100, 40))
        self.label_cur.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_cur.setFont(font)
        self.label_cur.setObjectName("label_cur")
        self.horizontalLayout_2.addWidget(self.label_cur)
        self.label_count = QtWidgets.QLabel(self.layoutWidget)
        self.label_count.setMinimumSize(QtCore.QSize(80, 40))
        self.label_count.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_count.setFont(font)
        self.label_count.setText("")
        self.label_count.setObjectName("label_count")
        self.horizontalLayout_2.addWidget(self.label_count)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 130, 218, 42))
        self.layoutWidget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setSpacing(36)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_curmac = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_curmac.setMinimumSize(QtCore.QSize(100, 40))
        self.label_curmac.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_curmac.setFont(font)
        self.label_curmac.setObjectName("label_curmac")
        self.horizontalLayout_6.addWidget(self.label_curmac)
        self.label_maccount = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_maccount.setMinimumSize(QtCore.QSize(80, 40))
        self.label_maccount.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_maccount.setFont(font)
        self.label_maccount.setText("")
        self.label_maccount.setObjectName("label_maccount")
        self.horizontalLayout_6.addWidget(self.label_maccount)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 40, 268, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_order = QtWidgets.QLabel(self.layoutWidget1)
        self.label_order.setMinimumSize(QtCore.QSize(80, 40))
        self.label_order.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_order.setFont(font)
        self.label_order.setObjectName("label_order")
        self.horizontalLayout_4.addWidget(self.label_order)
        self.lineedit_order = QtWidgets.QLabel(self.layoutWidget1)
        self.lineedit_order.setMinimumSize(QtCore.QSize(180, 40))
        self.lineedit_order.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_order.setFont(font)
        self.lineedit_order.setText("")
        self.lineedit_order.setObjectName("lineedit_order")
        self.horizontalLayout_4.addWidget(self.lineedit_order)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 270, 638, 120))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstRoundButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.firstRoundButton.setMinimumSize(QtCore.QSize(0, 118))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.firstRoundButton.setFont(font)
        self.firstRoundButton.setCheckable(False)
        self.firstRoundButton.setObjectName("firstRoundButton")
        self.horizontalLayout.addWidget(self.firstRoundButton)
        self.secondRoundButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.secondRoundButton.setMinimumSize(QtCore.QSize(0, 117))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.secondRoundButton.setFont(font)
        self.secondRoundButton.setCheckable(False)
        self.secondRoundButton.setObjectName("secondRoundButton")
        self.horizontalLayout.addWidget(self.secondRoundButton)
        self.printButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.printButton.setMinimumSize(QtCore.QSize(0, 118))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.printButton.setFont(font)
        self.printButton.setCheckable(False)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_query = QtWidgets.QAction(MainWindow)
        self.action_query.setObjectName("action_query")
        self.action_backupDB = QtWidgets.QAction(MainWindow)
        self.action_backupDB.setObjectName("action_backupDB")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_backupDB)
        self.menuTools.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "L6000烧录工具"))
        self.label_cur.setText(_translate("MainWindow", "当前设备数:"))
        self.label_curmac.setText(_translate("MainWindow", "可用MAC数:"))
        self.label_order.setText(_translate("MainWindow", "订单号:"))
        self.firstRoundButton.setText(_translate("MainWindow", "第一轮烧录"))
        self.secondRoundButton.setText(_translate("MainWindow", "第二轮烧录"))
        self.printButton.setText(_translate("MainWindow", "打印条码"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionHelp.setText(_translate("MainWindow", "软件使用说明"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.action_query.setText(_translate("MainWindow", "查询"))
        self.action_backupDB.setText(_translate("MainWindow", "备份数据库"))

