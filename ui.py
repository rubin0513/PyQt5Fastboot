# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fastboot.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import os
import subprocess
import struct

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from detectThread import *
from fastboot import lj_get_default_image_path

import common

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 30, 368, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_device_id = QtWidgets.QLabel(self.layoutWidget)
        self.label_device_id.setMinimumSize(QtCore.QSize(160, 40))
        self.label_device_id.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_device_id.setFont(font)
        self.label_device_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device_id.setWordWrap(False)
        self.label_device_id.setObjectName("label_device_id")
        self.horizontalLayout_3.addWidget(self.label_device_id, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser_device_id = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_device_id.setMinimumSize(QtCore.QSize(200, 40))
        self.textBrowser_device_id.setMaximumSize(QtCore.QSize(200, 40))
        self.textBrowser_device_id.setObjectName("textBrowser_device_id")
        self.horizontalLayout_3.addWidget(self.textBrowser_device_id)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 380, 667, 182))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_pmp = QtWidgets.QLabel(self.layoutWidget1)
        self.label_pmp.setMinimumSize(QtCore.QSize(160, 40))
        self.label_pmp.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pmp.setFont(font)
        self.label_pmp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pmp.setWordWrap(False)
        self.label_pmp.setObjectName("label_pmp")
        self.verticalLayout_3.addWidget(self.label_pmp)
        self.label_secboot = QtWidgets.QLabel(self.layoutWidget1)
        self.label_secboot.setMinimumSize(QtCore.QSize(160, 40))
        self.label_secboot.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_secboot.setFont(font)
        self.label_secboot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_secboot.setWordWrap(False)
        self.label_secboot.setObjectName("label_secboot")
        self.verticalLayout_3.addWidget(self.label_secboot)
        self.label_secos = QtWidgets.QLabel(self.layoutWidget1)
        self.label_secos.setMinimumSize(QtCore.QSize(160, 40))
        self.label_secos.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_secos.setFont(font)
        self.label_secos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_secos.setWordWrap(False)
        self.label_secos.setObjectName("label_secos")
        self.verticalLayout_3.addWidget(self.label_secos)
        self.label_uboot = QtWidgets.QLabel(self.layoutWidget1)
        self.label_uboot.setMinimumSize(QtCore.QSize(160, 40))
        self.label_uboot.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_uboot.setFont(font)
        self.label_uboot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_uboot.setWordWrap(False)
        self.label_uboot.setObjectName("label_uboot")
        self.verticalLayout_3.addWidget(self.label_uboot)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_pmp = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_pmp.setMinimumSize(QtCore.QSize(400, 40))
        self.lineEdit_pmp.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pmp.setFont(font)
        self.lineEdit_pmp.setText("")
        self.lineEdit_pmp.setObjectName("lineEdit_pmp")
        self.verticalLayout.addWidget(self.lineEdit_pmp)
        self.lineEdit_secboot = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_secboot.setMinimumSize(QtCore.QSize(400, 40))
        self.lineEdit_secboot.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_secboot.setFont(font)
        self.lineEdit_secboot.setObjectName("lineEdit_secboot")
        self.verticalLayout.addWidget(self.lineEdit_secboot)
        self.lineEdit_secos = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_secos.setMinimumSize(QtCore.QSize(400, 40))
        self.lineEdit_secos.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_secos.setFont(font)
        self.lineEdit_secos.setObjectName("lineEdit_secos")
        self.verticalLayout.addWidget(self.lineEdit_secos)
        self.lineEdit_uboot = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_uboot.setMinimumSize(QtCore.QSize(400, 40))
        self.lineEdit_uboot.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_uboot.setFont(font)
        self.lineEdit_uboot.setObjectName("lineEdit_uboot")
        self.verticalLayout.addWidget(self.lineEdit_uboot)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(8, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_burn_pmp = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_burn_pmp.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_pmp.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_pmp.setFont(font)
        self.button_burn_pmp.setObjectName("button_burn_pmp")
        self.verticalLayout_2.addWidget(self.button_burn_pmp)
        self.button_burn_secboot = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_burn_secboot.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_secboot.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_secboot.setFont(font)
        self.button_burn_secboot.setObjectName("button_burn_secboot")
        self.verticalLayout_2.addWidget(self.button_burn_secboot)
        self.button_burn_secos = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_burn_secos.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_secos.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_secos.setFont(font)
        self.button_burn_secos.setObjectName("button_burn_secos")
        self.verticalLayout_2.addWidget(self.button_burn_secos)
        self.button_burn_uboot = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_burn_uboot.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_uboot.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_uboot.setFont(font)
        self.button_burn_uboot.setObjectName("button_burn_uboot")
        self.verticalLayout_2.addWidget(self.button_burn_uboot)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(360, 590, 411, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_erase_all = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_erase_all.setMinimumSize(QtCore.QSize(80, 50))
        self.button_erase_all.setMaximumSize(QtCore.QSize(120, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.button_erase_all.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_erase_all.setFont(font)
        self.button_erase_all.setObjectName("button_erase_all")
        self.horizontalLayout_2.addWidget(self.button_erase_all)
        self.button_flash_all = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_flash_all.setMinimumSize(QtCore.QSize(80, 50))
        self.button_flash_all.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_flash_all.setFont(font)
        self.button_flash_all.setAutoDefault(False)
        self.button_flash_all.setDefault(False)
        self.button_flash_all.setFlat(False)
        self.button_flash_all.setObjectName("button_flash_all")
        self.horizontalLayout_2.addWidget(self.button_flash_all)
        self.button_reboot = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_reboot.setMinimumSize(QtCore.QSize(80, 50))
        self.button_reboot.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_reboot.setFont(font)
        self.button_reboot.setObjectName("button_reboot")
        self.horizontalLayout_2.addWidget(self.button_reboot)
        self.button_continue = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_continue.setMinimumSize(QtCore.QSize(80, 50))
        self.button_continue.setMaximumSize(QtCore.QSize(120, 50))
        self.button_continue.setObjectName("button_continue")
        self.horizontalLayout_2.addWidget(self.button_continue)
        self.button_flash_bbcb = QtWidgets.QPushButton(self.centralwidget)
        self.button_flash_bbcb.setGeometry(QtCore.QRect(410, 220, 80, 40))
        self.button_flash_bbcb.setMinimumSize(QtCore.QSize(80, 40))
        self.button_flash_bbcb.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_flash_bbcb.setFont(font)
        self.button_flash_bbcb.setObjectName("button_flash_bbcb")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(180, 133, 211, 224))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_manu_id = QtWidgets.QLabel(self.layoutWidget3)
        self.label_manu_id.setMinimumSize(QtCore.QSize(100, 30))
        self.label_manu_id.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_manu_id.setFont(font)
        self.label_manu_id.setObjectName("label_manu_id")
        self.horizontalLayout_17.addWidget(self.label_manu_id)
        self.lineEdit_manu_id = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_manu_id.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_manu_id.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_manu_id.setText("")
        self.lineEdit_manu_id.setObjectName("lineEdit_manu_id")
        self.horizontalLayout_17.addWidget(self.lineEdit_manu_id)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_hd_code = QtWidgets.QLabel(self.layoutWidget3)
        self.label_hd_code.setMinimumSize(QtCore.QSize(100, 30))
        self.label_hd_code.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_hd_code.setFont(font)
        self.label_hd_code.setObjectName("label_hd_code")
        self.horizontalLayout_16.addWidget(self.label_hd_code)
        self.lineEdit_hd_code = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_hd_code.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_hd_code.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_hd_code.setText("")
        self.lineEdit_hd_code.setObjectName("lineEdit_hd_code")
        self.horizontalLayout_16.addWidget(self.lineEdit_hd_code)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_loader_major = QtWidgets.QLabel(self.layoutWidget3)
        self.label_loader_major.setMinimumSize(QtCore.QSize(100, 30))
        self.label_loader_major.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_major.setFont(font)
        self.label_loader_major.setObjectName("label_loader_major")
        self.horizontalLayout_15.addWidget(self.label_loader_major)
        self.lineEdit_loader_major = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_loader_major.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_major.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_major.setText("")
        self.lineEdit_loader_major.setObjectName("lineEdit_loader_major")
        self.horizontalLayout_15.addWidget(self.lineEdit_loader_major)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_loader_minor = QtWidgets.QLabel(self.layoutWidget3)
        self.label_loader_minor.setMinimumSize(QtCore.QSize(100, 30))
        self.label_loader_minor.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_minor.setFont(font)
        self.label_loader_minor.setObjectName("label_loader_minor")
        self.horizontalLayout_14.addWidget(self.label_loader_minor)
        self.lineEdit_loader_minor = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_loader_minor.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_minor.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_minor.setText("")
        self.lineEdit_loader_minor.setObjectName("lineEdit_loader_minor")
        self.horizontalLayout_14.addWidget(self.lineEdit_loader_minor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_loader_type = QtWidgets.QLabel(self.layoutWidget3)
        self.label_loader_type.setMinimumSize(QtCore.QSize(100, 30))
        self.label_loader_type.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_type.setFont(font)
        self.label_loader_type.setObjectName("label_loader_type")
        self.horizontalLayout_5.addWidget(self.label_loader_type)
        self.lineEdit_loader_type = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_loader_type.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_type.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_loader_type.setText("")
        self.lineEdit_loader_type.setObjectName("lineEdit_loader_type")
        self.horizontalLayout_5.addWidget(self.lineEdit_loader_type)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_serial_number = QtWidgets.QLabel(self.layoutWidget3)
        self.label_serial_number.setMinimumSize(QtCore.QSize(100, 30))
        self.label_serial_number.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_serial_number.setFont(font)
        self.label_serial_number.setObjectName("label_serial_number")
        self.horizontalLayout_13.addWidget(self.label_serial_number)
        self.lineEdit_serial_number = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_serial_number.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_serial_number.setMaximumSize(QtCore.QSize(100, 30))
        self.lineEdit_serial_number.setText("")
        self.lineEdit_serial_number.setObjectName("lineEdit_serial_number")
        self.horizontalLayout_13.addWidget(self.lineEdit_serial_number)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(800, 10))
        self.statusbar.setMaximumSize(QtCore.QSize(800, 10))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setMinimumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_howto = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/howto.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("icon/howto.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action_howto.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.action_howto.setFont(font)
        self.action_howto.setObjectName("action_howto")
        self.action_about = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/qt.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/qt.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action_about.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.action_howto)
        self.menu.addSeparator()
        self.menu.addAction(self.action_about)
        self.menuBar.addAction(self.menu.menuAction())

        # get default image path info
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)

        self.lineEdit_pmp.setFont(font)
        self.lineEdit_secboot.setFont(font)
        self.lineEdit_secos.setFont(font)
        self.lineEdit_uboot.setFont(font)

        if(os.path.exists("toc\\pmp.toc")):
            self.lineEdit_pmp.setText(lj_get_default_image_path("toc\\pmp.toc"))

        if(os.path.exists("toc\\secboot.toc")):
            self.lineEdit_secboot.setText(lj_get_default_image_path("toc\\secboot.toc"))

        if(os.path.exists("toc\\secos.toc")):
            self.lineEdit_secos.setText(lj_get_default_image_path("toc\\secos.toc"))

        if(os.path.exists("toc\\u-boot.toc")):
            self.lineEdit_uboot.setText(lj_get_default_image_path("toc\\u-boot.toc"))

        self.retranslateUi(MainWindow)
        self.button_erase_all.clicked.connect(self.lj_erase_all)
        self.button_flash_all.clicked.connect(self.lj_flash_all)
        self.button_continue.clicked.connect(self.lj_continue)
        self.lineEdit_pmp.selectionChanged.connect(self.lj_select_pmp_image_file)
        self.lineEdit_secboot.selectionChanged.connect(self.lj_select_secboot_image_file)
        self.lineEdit_secos.selectionChanged.connect(self.lj_select_secos_image_file)
        self.lineEdit_uboot.selectionChanged.connect(self.lj_select_uboot_image_file)
        self.button_burn_pmp.clicked.connect(self.lj_flash_pmp)
        self.button_burn_secboot.clicked.connect(self.lj_flash_secboot)
        self.button_burn_secos.clicked.connect(self.lj_flash_secos)
        self.button_burn_uboot.clicked.connect(self.lj_flash_uboot)
        self.button_reboot.clicked.connect(self.lj_reboot)
        self.button_continue.clicked.connect(self.lj_continue)
        self.action_howto.triggered.connect(self.lj_help_howto)
        self.action_about.triggered.connect(self.lj_help_about)
        self.button_flash_bbcb.clicked.connect(self.lj_flash_nvram)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZX2000烧录工具"))
        self.label_device_id.setText(_translate("MainWindow", "发现设备"))
        self.label_pmp.setText(_translate("MainWindow", "pmp.toc路径"))
        self.label_secboot.setText(_translate("MainWindow", "secboot.toc路径"))
        self.label_secos.setText(_translate("MainWindow", "secos.toc路径"))
        self.label_uboot.setText(_translate("MainWindow", "u-boot.toc路径"))
        self.button_burn_pmp.setText(_translate("MainWindow", "烧录"))
        self.button_burn_secboot.setText(_translate("MainWindow", "烧录"))
        self.button_burn_secos.setText(_translate("MainWindow", "烧录"))
        self.button_burn_uboot.setText(_translate("MainWindow", "烧录"))
        self.button_erase_all.setText(_translate("MainWindow", "擦除所有分区"))
        self.button_flash_all.setText(_translate("MainWindow", "全部烧录"))
        self.button_reboot.setText(_translate("MainWindow", "重启设备"))
        self.button_continue.setText(_translate("MainWindow", "继续启动"))
        self.button_flash_bbcb.setText(_translate("MainWindow", "烧录BBCB"))
        self.label_manu_id.setText(_translate("MainWindow", "manufacturer_id"))
        self.label_hd_code.setText(_translate("MainWindow", "hardware_code"))
        self.label_loader_major.setText(_translate("MainWindow", "loader_major"))
        self.label_loader_minor.setText(_translate("MainWindow", "loader_minor"))
        self.label_loader_type.setText(_translate("MainWindow", "loader_type"))
        self.label_serial_number.setText(_translate("MainWindow", "serial_number"))
        self.menu.setTitle(_translate("MainWindow", "帮  助"))
        self.action_howto.setText(_translate("MainWindow", "使用手册"))
        self.action_about.setText(_translate("MainWindow", "关  于"))

    def startDetectDevice(self):
        self.detectThread = detectDeviceThread()
        self.detectThread.detectSignal.connect(self.onDeviceDetected)
        self.detectThread.start()

    def onDeviceDetected(self,data):

        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        self.textBrowser_device_id.setFont(font)

        if(common.PREVIOUS_DATA != data):
            common.PREVIOUS_DATA = data
            self.textBrowser_device_id.setText(data)

    '''
    实现所有的slots
    '''
    def lj_erase_all(self):
        '''

        :return:
        '''
        print("lj_erase_all.")

    def lj_flash_all(self):
        '''

        :return:
        '''
        # subprocess.Popen('fastboot.exe flashall',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    def lj_flash_pmp(self):
        '''
        烧写pmp镜像
        :return:
        '''
        flag = False
        fileName = self.lineEdit_pmp.text()
        command = common.FLASH_PREFIX + " " + common.PMP_ADDRESS + " " + fileName
        print("pmp command:",command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_pmp,"Error","pmp烧录失败")

    def lj_flash_secboot(self):
        '''
        烧写secboot镜像
        :return:
        '''
        flag = False
        fileName = self.lineEdit_secboot.text()
        command = common.FLASH_PREFIX + common.SECBOOT_ADDRESS + " " + fileName
        print("secboot command:",command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_secboot,"Error","secboot烧录失败")

    def lj_flash_secos(self):
        '''
        烧写secos镜像
        :return:
        '''
        fileName = self.lineEdit_secos.text()
        command = common.FLASH_PREFIX + common.SECOS_ADDRESS + " " + fileName
        print("secos command:",command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_secos,"Error","secos烧录失败")

    def lj_flash_uboot(self):
        '''
        烧写uboot镜像
        :return:
        '''
        fileName = self.lineEdit_uboot.text()
        command = common.FLASH_PREFIX + common.UBOOT_ADDRESS + " " + fileName
        print("uboot command:",command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,"Error","uboot烧录失败")

    def lj_load_default_bbcb(self):
        self.lineEdit_manu_id.setText("21")
        self.lineEdit_hd_code.setText("4")
        self.lineEdit_loader_major.setText("3")
        self.lineEdit_loader_minor.setText("1")
        self.lineEdit_loader_type.setText("1")
        self.lineEdit_serial_number.setText("1234")

    def lj_flash_nvram(self):
        '''
        BBCB和FIXINFO在nvram分区，其它数据在ljinfo分区
        :return:
        '''
        fp = open('toc\\nvram.bin',"rb+")

        # 写入hardware_code
        fp.seek(common.BBCB_OFFSET + 3)
        hardware_code = fp.read(1)

        hardware_code_new = int(self.lineEdit_hd_code.text())
        if(hardware_code != hardware_code_new):

            fp.seek(common.BBCB_OFFSET + 3)
            fp.write(struct.pack("B",hardware_code_new))
            fp.flush()

        # 写入serial_number
        serial_number = str(self.lineEdit_serial_number.text())
        fp.seek(common.BBCB_OFFSET + 7)
        fp.write(struct.pack("4s",bytes(serial_number,"utf-8")))
        fp.flush()

        # 计算BBCB结构体的crc值并写入结构体中
        fp.seek(common.BBCB_OFFSET)
        bbcb = fp.read(common.BBCB_STRUCT_SIZE)
        crcCommand = "crc.exe "+ str(bbcb)

        crcRet = subprocess.Popen(crcCommand,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        crc_new = crcRet.stdout.read()
        print("crc:",crc_new)
        fp.seek(common.BBCB_OFFSET)
        fp.write(struct.pack("2s",crc_new))
        fp.flush()

        fp.close()

        '''
        fp.seek(common.BBCB_OFFSET)
        crc,manufacturer_id,hardware_code,loader_major,loader_minor,loader_type,serial_number,random_number,padding \
            = struct.unpack("2sBBBBB4s4s9s",fp.read(common.BBCB_STRUCT_SIZE))
        print(crc,manufacturer_id,hardware_code,loader_major,loader_minor,loader_type,serial_number,random_number,padding)

        serial_number_new = struct.pack("<4s",b'0x12345678')
        hardware_code_new = 4

        bbcb = struct.pack("2sBBBBB4s4s9s",crc,manufacturer_id,hardware_code_new,loader_major,loader_minor,loader_type,serial_number_new,random_number,padding)
        crcCommand = "crc.exe "+ str(bbcb)
        print("crcCommand:",crcCommand)

        crcRet = subprocess.Popen(crcCommand,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        crc_new = crcRet.stdout.read()
        print("crc:",crc_new)

        fp.seek(common.BBCB_OFFSET)
        fp.write(struct.pack("2sBBBBB4s4s9s",crc_new,manufacturer_id,hardware_code,loader_major,loader_minor,loader_type,serial_number_new,random_number,padding))

        fp.close()
        '''

        command = "fastboot.exe flash " + common.NVRAM_ADDRESS + " toc\\nvram.bin"
        print(command)
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    def lj_flash_ljinfo(self):
        pass

    def lj_help_howto(self):
        '''
        打开软件使用帮助
        :return:
        '''

        QMessageBox.information(self.menu,"软件使用方法",common.HOWTOTEXT)

    def lj_help_about(self):
        '''
        显示软件相关信息
        :return:
        '''
        QMessageBox.aboutQt(self.menu,"PyQt5")

    def lj_reboot(self):
        '''
        重启设备
        :return:
        '''
        ret = subprocess.Popen('fastboot.exe reboot',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            print(line)

    def lj_continue(self):
        '''
        继续启动设备
        :return:
        '''
        ret = subprocess.Popen('fastboot.exe continue',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            print(line)

    def lj_select_pmp_image_file(self):
        '''
        打开boot.img文件选择框
        :return:
        '''
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_pmp,"请选择pmp镜像文件")
        print(fileName)
        if(len(fileName) != 0):
            self.lineEdit_pmp.setText(fileName)

    def lj_select_secboot_image_file(self):
        '''
        打开system.img文件选择框
        :return:
        '''
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secboot,"请选择secboot镜像文件")
        if(len(fileName) != 0):
            self.lineEdit_secboot.setText(fileName)

    def lj_select_secos_image_file(self):
        '''
        打开userdata.img文件选择框
        :return:
        '''
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secos,"请选择secos镜像文件")
        if(len(fileName) != 0):
            self.lineEdit_secos.setText(fileName)

    def lj_select_uboot_image_file(self):
        '''
        打开recovery.img文件选择框
        :return:
        '''
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_uboot,"请选择uboot镜像文件")
        if(len(fileName) != 0):
            self.lineEdit_uboot.setText(fileName)