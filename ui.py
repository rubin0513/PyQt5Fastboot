# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/djstava/Workshop/Github/PyQt5Fastboot/fastboot.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import os
import subprocess
import struct
import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from detectThread import *
from fastboot import lj_get_default_image_path
from fastboot import lj_generate_random_number

import common
import showPlatform

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/lj.jpg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 620, 411, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_flash_all = QtWidgets.QPushButton(self.layoutWidget)
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
        self.button_reboot = QtWidgets.QPushButton(self.layoutWidget)
        self.button_reboot.setMinimumSize(QtCore.QSize(80, 50))
        self.button_reboot.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_reboot.setFont(font)
        self.button_reboot.setObjectName("button_reboot")
        self.horizontalLayout_2.addWidget(self.button_reboot)
        self.button_continue = QtWidgets.QPushButton(self.layoutWidget)
        self.button_continue.setMinimumSize(QtCore.QSize(80, 50))
        self.button_continue.setMaximumSize(QtCore.QSize(120, 50))
        self.button_continue.setObjectName("button_continue")
        self.horizontalLayout_2.addWidget(self.button_continue)
        self.button_flash_bbcb = QtWidgets.QPushButton(self.centralwidget)
        self.button_flash_bbcb.setGeometry(QtCore.QRect(580, 140, 80, 40))
        self.button_flash_bbcb.setMinimumSize(QtCore.QSize(80, 40))
        self.button_flash_bbcb.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_flash_bbcb.setFont(font)
        self.button_flash_bbcb.setObjectName("button_flash_bbcb")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 60, 233, 204))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_manu_id = QtWidgets.QLabel(self.layoutWidget1)
        self.label_manu_id.setMinimumSize(QtCore.QSize(110, 20))
        self.label_manu_id.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_manu_id.setFont(font)
        self.label_manu_id.setObjectName("label_manu_id")
        self.verticalLayout_5.addWidget(self.label_manu_id)
        self.label_hd_code = QtWidgets.QLabel(self.layoutWidget1)
        self.label_hd_code.setMinimumSize(QtCore.QSize(110, 20))
        self.label_hd_code.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_hd_code.setFont(font)
        self.label_hd_code.setObjectName("label_hd_code")
        self.verticalLayout_5.addWidget(self.label_hd_code)
        self.label_loader_major = QtWidgets.QLabel(self.layoutWidget1)
        self.label_loader_major.setMinimumSize(QtCore.QSize(110, 20))
        self.label_loader_major.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_major.setFont(font)
        self.label_loader_major.setObjectName("label_loader_major")
        self.verticalLayout_5.addWidget(self.label_loader_major)
        self.label_loader_minor = QtWidgets.QLabel(self.layoutWidget1)
        self.label_loader_minor.setMinimumSize(QtCore.QSize(110, 20))
        self.label_loader_minor.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_minor.setFont(font)
        self.label_loader_minor.setObjectName("label_loader_minor")
        self.verticalLayout_5.addWidget(self.label_loader_minor)
        self.label_loader_type = QtWidgets.QLabel(self.layoutWidget1)
        self.label_loader_type.setMinimumSize(QtCore.QSize(110, 20))
        self.label_loader_type.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_loader_type.setFont(font)
        self.label_loader_type.setObjectName("label_loader_type")
        self.verticalLayout_5.addWidget(self.label_loader_type)
        self.label_serial_number = QtWidgets.QLabel(self.layoutWidget1)
        self.label_serial_number.setMinimumSize(QtCore.QSize(110, 20))
        self.label_serial_number.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_serial_number.setFont(font)
        self.label_serial_number.setObjectName("label_serial_number")
        self.verticalLayout_5.addWidget(self.label_serial_number)
        self.label_random_number = QtWidgets.QLabel(self.layoutWidget1)
        self.label_random_number.setMinimumSize(QtCore.QSize(110, 20))
        self.label_random_number.setMaximumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_random_number.setFont(font)
        self.label_random_number.setObjectName("label_random_number")
        self.verticalLayout_5.addWidget(self.label_random_number)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(8, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_manu_id = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_manu_id.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_manu_id.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_manu_id.setFont(font)
        self.lineEdit_manu_id.setText("")
        self.lineEdit_manu_id.setObjectName("lineEdit_manu_id")
        self.verticalLayout_4.addWidget(self.lineEdit_manu_id)
        self.lineEdit_hd_code = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_hd_code.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_hd_code.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_hd_code.setFont(font)
        self.lineEdit_hd_code.setText("")
        self.lineEdit_hd_code.setObjectName("lineEdit_hd_code")
        self.verticalLayout_4.addWidget(self.lineEdit_hd_code)
        self.lineEdit_loader_major = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_loader_major.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_loader_major.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_loader_major.setFont(font)
        self.lineEdit_loader_major.setText("")
        self.lineEdit_loader_major.setObjectName("lineEdit_loader_major")
        self.verticalLayout_4.addWidget(self.lineEdit_loader_major)
        self.lineEdit_loader_minor_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_loader_minor_2.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_loader_minor_2.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_loader_minor_2.setFont(font)
        self.lineEdit_loader_minor_2.setText("")
        self.lineEdit_loader_minor_2.setObjectName("lineEdit_loader_minor_2")
        self.verticalLayout_4.addWidget(self.lineEdit_loader_minor_2)
        self.lineEdit_loader_type = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_loader_type.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_loader_type.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_loader_type.setFont(font)
        self.lineEdit_loader_type.setText("")
        self.lineEdit_loader_type.setObjectName("lineEdit_loader_type")
        self.verticalLayout_4.addWidget(self.lineEdit_loader_type)
        self.lineEdit_serial_number = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_serial_number.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_serial_number.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_serial_number.setFont(font)
        self.lineEdit_serial_number.setText("")
        self.lineEdit_serial_number.setObjectName("lineEdit_serial_number")
        self.verticalLayout_4.addWidget(self.lineEdit_serial_number)
        self.lineEdit_random_number = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_random_number.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_random_number.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_random_number.setFont(font)
        self.lineEdit_random_number.setText("")
        self.lineEdit_random_number.setObjectName("lineEdit_random_number")
        self.verticalLayout_4.addWidget(self.lineEdit_random_number)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(170, 270, 716, 344))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_pmp = QtWidgets.QLabel(self.layoutWidget2)
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
        self.label_secboot = QtWidgets.QLabel(self.layoutWidget2)
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
        self.label_secos = QtWidgets.QLabel(self.layoutWidget2)
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
        self.label_uboot = QtWidgets.QLabel(self.layoutWidget2)
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
        self.label_dev_tree = QtWidgets.QLabel(self.layoutWidget2)
        self.label_dev_tree.setMinimumSize(QtCore.QSize(160, 40))
        self.label_dev_tree.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_dev_tree.setFont(font)
        self.label_dev_tree.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dev_tree.setWordWrap(False)
        self.label_dev_tree.setObjectName("label_dev_tree")
        self.verticalLayout_3.addWidget(self.label_dev_tree)
        self.label_otaloader = QtWidgets.QLabel(self.layoutWidget2)
        self.label_otaloader.setMinimumSize(QtCore.QSize(160, 40))
        self.label_otaloader.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_otaloader.setFont(font)
        self.label_otaloader.setAlignment(QtCore.Qt.AlignCenter)
        self.label_otaloader.setWordWrap(False)
        self.label_otaloader.setObjectName("label_otaloader")
        self.verticalLayout_3.addWidget(self.label_otaloader)
        self.label_splash = QtWidgets.QLabel(self.layoutWidget2)
        self.label_splash.setMinimumSize(QtCore.QSize(160, 40))
        self.label_splash.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_splash.setFont(font)
        self.label_splash.setAlignment(QtCore.Qt.AlignCenter)
        self.label_splash.setWordWrap(False)
        self.label_splash.setObjectName("label_splash")
        self.verticalLayout_3.addWidget(self.label_splash)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_pmp = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_pmp.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_pmp.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pmp.setFont(font)
        self.lineEdit_pmp.setText("")
        self.lineEdit_pmp.setObjectName("lineEdit_pmp")
        self.verticalLayout_2.addWidget(self.lineEdit_pmp)
        self.lineEdit_secboot = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_secboot.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_secboot.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_secboot.setFont(font)
        self.lineEdit_secboot.setObjectName("lineEdit_secboot")
        self.verticalLayout_2.addWidget(self.lineEdit_secboot)
        self.lineEdit_secos = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_secos.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_secos.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_secos.setFont(font)
        self.lineEdit_secos.setObjectName("lineEdit_secos")
        self.verticalLayout_2.addWidget(self.lineEdit_secos)
        self.lineEdit_uboot = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_uboot.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_uboot.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_uboot.setFont(font)
        self.lineEdit_uboot.setObjectName("lineEdit_uboot")
        self.verticalLayout_2.addWidget(self.lineEdit_uboot)
        self.lineEdit_dev_tree = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_dev_tree.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_dev_tree.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_dev_tree.setFont(font)
        self.lineEdit_dev_tree.setObjectName("lineEdit_dev_tree")
        self.verticalLayout_2.addWidget(self.lineEdit_dev_tree)
        self.lineEdit_otaloader = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_otaloader.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_otaloader.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_otaloader.setFont(font)
        self.lineEdit_otaloader.setObjectName("lineEdit_otaloader")
        self.verticalLayout_2.addWidget(self.lineEdit_otaloader)
        self.lineEdit_splash = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_splash.setMinimumSize(QtCore.QSize(450, 40))
        self.lineEdit_splash.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_splash.setFont(font)
        self.lineEdit_splash.setObjectName("lineEdit_splash")
        self.verticalLayout_2.addWidget(self.lineEdit_splash)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_burn_pmp = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_pmp.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_pmp.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_pmp.setFont(font)
        self.button_burn_pmp.setObjectName("button_burn_pmp")
        self.verticalLayout.addWidget(self.button_burn_pmp)
        self.button_burn_secboot = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_secboot.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_secboot.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_secboot.setFont(font)
        self.button_burn_secboot.setObjectName("button_burn_secboot")
        self.verticalLayout.addWidget(self.button_burn_secboot)
        self.button_burn_secos = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_secos.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_secos.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_secos.setFont(font)
        self.button_burn_secos.setObjectName("button_burn_secos")
        self.verticalLayout.addWidget(self.button_burn_secos)
        self.button_burn_uboot = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_uboot.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_uboot.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_uboot.setFont(font)
        self.button_burn_uboot.setObjectName("button_burn_uboot")
        self.verticalLayout.addWidget(self.button_burn_uboot)
        self.button_burn_devtree = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_devtree.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_devtree.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_devtree.setFont(font)
        self.button_burn_devtree.setObjectName("button_burn_devtree")
        self.verticalLayout.addWidget(self.button_burn_devtree)
        self.button_burn_otaloader = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_otaloader.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_otaloader.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_otaloader.setFont(font)
        self.button_burn_otaloader.setObjectName("button_burn_otaloader")
        self.verticalLayout.addWidget(self.button_burn_otaloader)
        self.button_burn_splash = QtWidgets.QPushButton(self.layoutWidget2)
        self.button_burn_splash.setMinimumSize(QtCore.QSize(80, 40))
        self.button_burn_splash.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.button_burn_splash.setFont(font)
        self.button_burn_splash.setObjectName("button_burn_splash")
        self.verticalLayout.addWidget(self.button_burn_splash)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 10, 370, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_device_id = QtWidgets.QLabel(self.widget)
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
        self.horizontalLayout_3.addWidget(self.label_device_id)
        self.lineEdit_device_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_device_id.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_device_id.setMaximumSize(QtCore.QSize(200, 40))
        self.lineEdit_device_id.setObjectName("lineEdit_device_id")
        self.horizontalLayout_3.addWidget(self.lineEdit_device_id)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMinimumSize(QtCore.QSize(800, 10))
        self.statusbar.setMaximumSize(QtCore.QSize(800, 10))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1080, 22))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/howto.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/howto.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action_howto.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.action_howto.setFont(font)
        self.action_howto.setObjectName("action_howto")
        self.action_about = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/qt.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("icon/qt.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.action_about.setIcon(icon2)
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
        self.lineEdit_dev_tree.setFont(font)
        self.lineEdit_otaloader.setFont(font)

        if showPlatform.OS_WIN:
            if(os.path.exists("toc\\pmp.toc")):
                self.lineEdit_pmp.setText(lj_get_default_image_path("toc\\pmp.toc"))

            if(os.path.exists("toc\\secboot.toc")):
                self.lineEdit_secboot.setText(lj_get_default_image_path("toc\\secboot.toc"))

            if(os.path.exists("toc\\secos.toc")):
                self.lineEdit_secos.setText(lj_get_default_image_path("toc\\secos.toc"))

            if(os.path.exists("toc\\u-boot.toc")):
                self.lineEdit_uboot.setText(lj_get_default_image_path("toc\\u-boot.toc"))

            if(os.path.exists("toc\\devicetree.img")):
                self.lineEdit_dev_tree.setText(lj_get_default_image_path("toc\\devicetree.img"))

            if(os.path.exists("toc\\otaloader.img")):
                self.lineEdit_otaloader.setText(lj_get_default_image_path("toc\\otaloader.img"))
            if(os.path.exists("toc\\splash.dat")):
                self.lineEdit_splash.setText(lj_get_default_image_path("toc\\splash.dat"))
        else:
            if(os.path.exists("toc/pmp.toc")):
                self.lineEdit_pmp.setText(lj_get_default_image_path("toc/pmp.toc"))

            if(os.path.exists("toc/secboot.toc")):
                self.lineEdit_secboot.setText(lj_get_default_image_path("toc/secboot.toc"))

            if(os.path.exists("toc/secos.toc")):
                self.lineEdit_secos.setText(lj_get_default_image_path("toc/secos.toc"))

            if(os.path.exists("toc/u-boot.toc")):
                self.lineEdit_uboot.setText(lj_get_default_image_path("toc/u-boot.toc"))

            if(os.path.exists("toc/devicetree.img")):
                self.lineEdit_dev_tree.setText(lj_get_default_image_path("toc/devicetree.img"))

            if(os.path.exists("toc/otaloader.img")):
                self.lineEdit_otaloader.setText(lj_get_default_image_path("toc/otaloader.img"))
            if(os.path.exists("toc/splash.dat")):
                self.lineEdit_splash.setText(lj_get_default_image_path("toc/splash.dat"))

        self.retranslateUi(MainWindow)

        self.lineEdit_pmp.selectionChanged.connect(self.lj_select_pmp_image_file)
        self.lineEdit_secboot.selectionChanged.connect(self.lj_select_secboot_image_file)
        self.lineEdit_secos.selectionChanged.connect(self.lj_select_secos_image_file)
        self.lineEdit_uboot.selectionChanged.connect(self.lj_select_uboot_image_file)
        self.lineEdit_dev_tree.selectionChanged.connect(self.lj_select_devtree_image_file)
        self.lineEdit_otaloader.selectionChanged.connect(self.lj_select_otaloader_file)
        self.lineEdit_splash.selectionChanged.connect(self.lj_select_splash_file)

        self.button_flash_bbcb.clicked.connect(self.lj_flash_nvram)
        self.button_burn_pmp.clicked.connect(self.lj_flash_pmp)
        self.button_burn_secboot.clicked.connect(self.lj_flash_secboot)
        self.button_burn_secos.clicked.connect(self.lj_flash_secos)
        self.button_burn_uboot.clicked.connect(self.lj_flash_uboot)
        self.button_burn_devtree.clicked.connect(self.lj_flash_dev_tree)
        self.button_burn_otaloader.clicked.connect(self.lj_flash_otaloader)
        self.button_burn_splash.clicked.connect(self.lj_flash_splash)

        self.button_flash_all.clicked.connect(self.lj_flash_all)
        self.button_reboot.clicked.connect(self.lj_reboot)
        self.button_continue.clicked.connect(self.lj_continue)

        self.action_howto.triggered.connect(self.lj_help_howto)
        self.action_about.triggered.connect(self.lj_help_about)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZX2000烧录工具"))
        self.button_flash_all.setText(_translate("MainWindow", "一键烧录"))
        self.button_reboot.setText(_translate("MainWindow", "重启设备"))
        self.button_continue.setText(_translate("MainWindow", "继续启动"))
        self.button_flash_bbcb.setText(_translate("MainWindow", "烧录BBCB"))
        self.label_manu_id.setText(_translate("MainWindow", "manufacturer_id"))
        self.label_hd_code.setText(_translate("MainWindow", "hardware_code"))
        self.label_loader_major.setText(_translate("MainWindow", "loader_major"))
        self.label_loader_minor.setText(_translate("MainWindow", "loader_minor"))
        self.label_loader_type.setText(_translate("MainWindow", "loader_type"))
        self.label_serial_number.setText(_translate("MainWindow", "serial_number"))
        self.label_random_number.setText(_translate("MainWindow", "random_number"))
        self.label_pmp.setText(_translate("MainWindow", "pmp.toc路径"))
        self.label_secboot.setText(_translate("MainWindow", "secboot.toc路径"))
        self.label_secos.setText(_translate("MainWindow", "secos.toc路径"))
        self.label_uboot.setText(_translate("MainWindow", "u-boot.toc路径"))
        self.label_dev_tree.setText(_translate("MainWindow", "dev_Tree路径"))
        self.label_otaloader.setText(_translate("MainWindow", "otaloader路径"))
        self.label_splash.setText(_translate("MainWindow", "splash路径"))
        self.button_burn_pmp.setText(_translate("MainWindow", "烧录"))
        self.button_burn_secboot.setText(_translate("MainWindow", "烧录"))
        self.button_burn_secos.setText(_translate("MainWindow", "烧录"))
        self.button_burn_uboot.setText(_translate("MainWindow", "烧录"))
        self.button_burn_devtree.setText(_translate("MainWindow", "烧录"))
        self.button_burn_otaloader.setText(_translate("MainWindow", "烧录"))
        self.button_burn_splash.setText(_translate("MainWindow", "烧录"))
        self.label_device_id.setText(_translate("MainWindow", "发现设备"))
        self.menu.setTitle(_translate("MainWindow", "帮  助"))
        self.action_howto.setText(_translate("MainWindow", "使用手册"))
        self.action_about.setText(_translate("MainWindow", "关  于"))

    def startDetectDevice(self):
        '''
        开启线程，检测Android设备上线
        :return:
        '''
        self.detectThread = detectDeviceThread()
        self.detectThread.detectSignal.connect(self.onDeviceDetected)
        self.detectThread.start()

    def onDeviceDetected(self,data):
        '''
        检测到Android设备上线后的操作
        :return:
        '''

        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_device_id.setFont(font)

        if data != self.lineEdit_device_id.text():
            self.lineEdit_device_id.setText(data)
            if data.strip():
                common.FLAG_DEVICE_ONLINE = True
            else:
                common.FLAG_DEVICE_ONLINE = False
        else:
                if data.strip():
                    common.FLAG_DEVICE_ONLINE = True
                else:
                    common.FLAG_DEVICE_ONLINE = False

    '''
    实现所有的slots
    '''
    def lj_flash_all(self):
        '''
        一键烧录
        :return:
        '''
        flag_pmp = True
        flag_secboot = True
        flag_secos = True
        flag_uboot = True
        flag_uboot_bak = True
        flag_bbcb = True
        flag_devtree = True
        flag_splash = True
        flag_otaloader = True

        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_flash_all,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if len(self.lineEdit_serial_number.text()) != 8:
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,"序列号必须是8位")
            return

        if len(self.lineEdit_random_number.text()) != 8:
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,"random number必须是8位")
            return

        if len(self.lineEdit_pmp.text()) == 0:
            QMessageBox.critical(self.button_flash_all,common.BURNERROR,"没有找到pmp镜像!")
            return
        else:
            flag_pmp = self.lj_flash_pmp_all(self.lineEdit_pmp.text())
            logging.debug("flash pmp result: " + flag_pmp.__str__())
            time.sleep(1)

        if flag_pmp:
            QMessageBox.critical(self.button_flash_all,common.BURNERROR,"初始化失败，请重新烧录pmp镜像!!")
            return

        if len(self.lineEdit_secboot.text()) != 0:
            flag_secboot = self.lj_flash_secboot_all(self.lineEdit_secboot.text())
        else:
            flag_secboot = False

        if len(self.lineEdit_secos.text()) != 0:
            flag_secos = self.lj_flash_secos_all(self.lineEdit_secos.text())
        else:
            flag_secos = False

        if len(self.lineEdit_uboot.text()) != 0:
            flag_uboot,flag_uboot_bak = self.lj_flash_uboot_all(self.lineEdit_uboot.text())
        else:
            flag_uboot = False
            flag_uboot_bak = False

        flag_bbcb = self.lj_flash_nvram_all()

        if len(self.lineEdit_dev_tree.text()) != 0:
            flag_devtree = self.lj_flash_dev_tree_all(self.lineEdit_dev_tree.text())
        else:
            flag_devtree = False

        if len(self.lineEdit_otaloader.text()):
            flag_otaloader = self.lj_flash_otaloader_all(self.lineEdit_otaloader.text())
        else:
            flag_otaloader = False

        if len(self.lineEdit_splash.text()) != 0:
            flag_splash = self.lj_flash_splash_all(self.lineEdit_splash.text())
        else:
            flag_splash = False

        logging.debug("flash secboot result:" + flag_secboot.__str__())
        logging.debug("flash secos result: " + flag_secos.__str__())
        logging.debug("flash uboot result: " + flag_uboot.__str__())
        logging.debug("flash ubootbak result: " + flag_uboot_bak.__str__())
        logging.debug("flash bbcb result: " + flag_bbcb.__str__())
        logging.debug("flash devtree result: " + flag_devtree.__str__())
        logging.debug("flash splash result: " + flag_splash.__str__())
        logging.debug("flash otaloader result: " + flag_otaloader.__str__())

        message_secboot = "secboot " if flag_secboot else ""
        message_secos = "secos " if flag_secos else ""
        message_uboot = "uboot " if flag_uboot else ""
        message_ubootbak = "ubootbak " if flag_uboot_bak else ""
        message_bbcb = "bbcb " if flag_bbcb else ""
        message_devtree = "devtree " if flag_devtree else ""
        message_splash = "splash " if flag_splash else ""
        message_otaloader = "otaloader " if flag_otaloader else ""

        if (not flag_pmp) and (not flag_secboot) and (not flag_secos) and (not flag_bbcb) and (not flag_uboot) and (not flag_uboot_bak) and (not flag_devtree) \
                and (not flag_splash) and (not flag_otaloader):
            message = common.TEXT_FLASH_SUCCESS
        else:
            message = common.TEXT_FLASH_FAILED_PREFIX + message_secboot + message_secos + message_uboot + message_ubootbak + message_bbcb + message_devtree \
                + message_splash + message_otaloader + common.TEXT_FLASH_FAILED_SUFFIX

        QtWidgets.QMessageBox.information(self.button_flash_all,common.TEXT_FLASH_TITLE,message)

    def lj_flash_pmp(self):
        '''
        烧写pmp镜像
        :return:
        '''

        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_pmp,common.BURNERROR,common.DEVICENOTONLINE)
            return

        logging.debug("\r\n")
        flag = False
        fileName = self.lineEdit_pmp.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_pmp,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.PMP_ADDRESS + fileName
        logging.debug("pmp command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            common.FLAG_PMP_FLASHED = False
            QtWidgets.QMessageBox.critical(self.button_burn_pmp,common.BURNERROR,"pmp烧录失败")
        else:
            common.FLAG_PMP_FLASHED = True
            QtWidgets.QMessageBox.information(self.button_burn_pmp,common.BURNSUCCESS,"pmp烧录成功")

    def lj_flash_secboot(self):
        '''
        烧写secboot镜像
        :return:
        '''
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_secboot,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_secboot,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        flag = False
        fileName = self.lineEdit_secboot.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_secboot,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.SECBOOT_ADDRESS + " " + fileName
        logging.debug("secboot command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_secboot,common.BURNERROR,"secboot烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_secboot,common.BURNSUCCESS,"secboot烧录成功")

    def lj_flash_secos(self):
        '''
        烧写secos镜像
        :return:
        '''
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_secos,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_secos,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        fileName = self.lineEdit_secos.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_secos,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.SECOS_ADDRESS + " " + fileName
        logging.debug("secos command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_secos,common.BURNERROR,"secos烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_secos,common.BURNSUCCESS,"secos烧录成功")

    def lj_flash_uboot(self):
        '''
        烧写uboot镜像
        :return:
        '''
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        fileName = self.lineEdit_uboot.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.UBOOT_ADDRESS + " " + fileName
        logging.debug("uboot command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,common.BURNERROR,"uboot烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_uboot,common.BURNSUCCESS,"uboot烧录成功")

        # uboot_backup
        command_bak = common.FLASH_PREFIX + common.UBOOT_BACK_ADDRESS + " " + fileName
        logging.debug("uboot backup command:" + command_bak)

        ret_bak = subprocess.Popen(command_bak,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret_bak.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag_bak = True
                break
            else:
                flag_bak = False

        ret.wait()

        if(flag_bak == True):
            QtWidgets.QMessageBox.critical(self.button_burn_uboot,common.BURNERROR,"uboot备份烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_uboot,common.BURNSUCCESS,"uboot备份烧录成功")

    def lj_flash_dev_tree(self):
        '''
        烧写device tree镜像
        :return:
        '''

        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_devtree,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_devtree,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        fileName = self.lineEdit_dev_tree.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_devtree,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.DEVICETREE_ADDRESS + " " + fileName
        logging.debug("device tree command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_devtree,common.BURNERROR,"device tree烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_devtree,common.BURNSUCCESS,"device tree烧录成功")

    def lj_flash_otaloader(self):
        '''
        烧写otaloader镜像
        :return:
        '''

        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_otaloader,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_otaloader,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        fileName = self.lineEdit_otaloader.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_otaloader,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.KERNELOTA_ADDRESS + " " + fileName
        logging.debug("otaloader command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                ret.stdout.close()
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_otaloader,common.BURNERROR,"otaloader烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_otaloader,common.BURNSUCCESS,"otaloader烧录成功")

    def lj_flash_splash(self):
        '''
        烧写splash镜像
        :return:
        '''

        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_burn_splash,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_burn_splash,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")
        fileName = self.lineEdit_splash.text()
        if(len(fileName) == 0):
            QtWidgets.QMessageBox.critical(self.button_burn_splash,common.BURNERROR,common.SELECTIMAGEFILE)
            return

        command = common.FLASH_PREFIX + common.SPLASH_ADDRESS + " " + fileName
        logging.debug("splash command:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_burn_splash,common.BURNERROR,"splash烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_burn_splash,common.BURNSUCCESS,"splash烧录成功")

    def lj_load_default_bbcb(self):
        self.lineEdit_manu_id.setText("21")
        self.lineEdit_hd_code.setText("4")
        self.lineEdit_loader_major.setText("3")
        self.lineEdit_loader_minor_2.setText("1")
        self.lineEdit_loader_type.setText("1")
        self.lineEdit_serial_number.setText("1234")
        # self.lineEdit_random_number.setText("5678")

    def lj_flash_nvram(self):
        '''
        BBCB和FIXINFO在nvram分区，其它数据在ljinfo分区
        :return:
        '''

        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.PMPISNOTFLASHED)
            return

        logging.debug("\r\n")

        if showPlatform.OS_WIN:
            fp = open('toc\\nvram.bin',"rb+")
        else:
            fp = open('toc/nvram.bin',"rb+")

        #写入manufacturer id
        fp.seek(common.BBCB_OFFSET + 2,os.SEEK_SET)
        manufacturer_id = fp.read(1)
        manufacturer_id_new = int(self.lineEdit_manu_id.text())
        if(manufacturer_id != manufacturer_id_new):
            logging.debug("new manufacturer_id: " + str(manufacturer_id_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",manufacturer_id_new))
            fp.flush()

        # 写入hardware_code
        hardware_code = fp.read(1)
        hardware_code_new = int(self.lineEdit_hd_code.text())
        if(hardware_code != hardware_code_new):
            logging.debug("write new hardware_code: " + str(hardware_code_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",hardware_code_new))
            fp.flush()

        # 写入loader_major
        loader_major = fp.read(1)
        loader_major_new = int(self.lineEdit_loader_major.text())
        if(loader_major != loader_major_new):
            logging.debug("write new loader_major: " + str(loader_major_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_major_new))
            fp.flush()

        # 写入loader_minor
        loader_minor = fp.read(1)
        loader_minor_new = int(self.lineEdit_loader_minor_2.text())
        if(loader_minor != loader_minor_new):
            logging.debug("write new loader_minor: " + str(loader_minor_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_minor_new))
            fp.flush()

        # 写入loader_type
        loader_type = fp.read(1)
        loader_type_new = int(self.lineEdit_loader_type.text())
        if(loader_type != loader_type_new):
            logging.debug("write new loader_type: " + str(loader_type_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_type_new))
            fp.flush()

        # 写入serial_number
        serial_number = str(self.lineEdit_serial_number.text())
        logging.debug("input serial number: " + serial_number)

        if(len(serial_number) != 8):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,"序列号必须是8位")
            return

        # 以BCD码显示serial number
        fp.write(struct.pack("B",int(serial_number[0:2],16)))
        fp.write(struct.pack("B",int(serial_number[2:4],16)))
        fp.write(struct.pack("B",int(serial_number[4:6],16)))
        fp.write(struct.pack("B",int(serial_number[6:8],16)))
        fp.flush()

        # 写入random number
        random_number = str(self.lineEdit_random_number.text())
        if(len(random_number) == 0):
            random_number_new = str(lj_generate_random_number())
            logging.debug("generate random number: " + str(random_number_new))

            fp.write(struct.pack("B",int(random_number_new[0:2],16)))
            fp.write(struct.pack("B",int(random_number_new[2:4],16)))
            fp.write(struct.pack("B",int(random_number_new[4:6],16)))
            fp.write(struct.pack("B",int(random_number_new[6:8],16)))

        elif(len(random_number) != 8):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,"random number必须是8位")
            return
        else:
            fp.write(struct.pack("B",int(random_number[0:2],16)))
            fp.write(struct.pack("B",int(random_number[2:4],16)))
            fp.write(struct.pack("B",int(random_number[4:6],16)))
            fp.write(struct.pack("B",int(random_number[6:8],16)))

        fp.flush()

        # 计算BBCB结构体的crc值并写入结构体中
        fp.seek(common.BBCB_OFFSET,os.SEEK_SET)
        bbcb = fp.read(common.BBCB_STRUCT_SIZE)
        crcCommand = "crcForBurnTool.exe "+ str(bbcb)

        crcRet = subprocess.Popen(crcCommand,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        crc_new = crcRet.stdout.read()
        logging.debug("crc:" + str(crc_new))

        fp.seek(common.BBCB_OFFSET,os.SEEK_SET)
        fp.write(struct.pack("2s",crc_new))
        fp.flush()

        fp.close()

        if showPlatform.OS_WIN:
            command = common.FLASH_PREFIX + common.NVRAM_ADDRESS + " toc\\nvram.bin"
        else:
            command = common.FLASH_PREFIX + common.NVRAM_ADDRESS + " toc/nvram.bin"

        logging.debug("nvram command: " + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        if(flag == True):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,"BBCB烧录失败")
        else:
            QtWidgets.QMessageBox.information(self.button_flash_bbcb,common.BURNSUCCESS,"BBCB烧录成功")

    def lj_flash_ljinfo(self):
        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.PMPISNOTFLASHED)
            return

    def lj_help_howto(self):
        '''
        打开软件使用帮助
        :return:
        '''

        QtWidgets.QMessageBox.information(self.menuBar,common.HOWTOUSE,common.HOWTOTEXT)

    def lj_help_about(self):
        '''
        显示软件相关信息
        :return:
        '''

        QMessageBox.aboutQt(self.menuBar,"PyQt5")

    def lj_reboot(self):
        '''
        重启设备
        :return:
        '''

        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_reboot,common.BURNERROR,common.DEVICENOTONLINE)
            return

        logging.debug("\r\n")
        ret = subprocess.Popen(common.FLASH_REBOOT,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)

    def lj_continue(self):
        '''
        继续启动设备
        :return:
        '''

        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_continue,common.BURNERROR,common.DEVICENOTONLINE)
            return

        logging.debug("\r\n")
        ret = subprocess.Popen(common.FLASH_CONTINUE,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)

    def lj_select_pmp_image_file(self):
        '''
        打开pmp文件选择框
        :return:
        '''

        fileName,_ = QtWidgets.QFileDialog.getOpenFileName(self.lineEdit_pmp,"请选择pmp镜像文件"," ","pmp files(*.toc)")
        logging.debug("lj_select_pmp_image_file" + fileName)
        if fileName:
            if (fileName != common.PMP_DEFAULT_FILE_PATH):
                self.lineEdit_pmp.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_secboot_image_file(self):
        '''
        打开secboot文件选择框
        :return:
        '''

        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secboot,"请选择secboot镜像文件"," ","secboot files(*.toc)")
        logging.debug("lj_select_secboot_image_file" + fileName)
        if fileName:
            if (fileName != common.SECBOOT_DEFAULT_FILE_PATH):
                self.lineEdit_secboot.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_secos_image_file(self):
        '''
        打开secos文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secos,"请选择secos镜像文件"," ","secos files(*.toc)")
        logging.debug("lj_select_secos_image_file" + fileName)
        if fileName:
            if (fileName != common.SECOS_DEFAULT_FILE_PATH):
                self.lineEdit_secos.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_uboot_image_file(self):
        '''
        打开uboot文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_uboot,"请选择uboot镜像文件"," ","uboot files(*.toc)")
        logging.debug("lj_select_uboot_image_file" + fileName)
        if fileName:
            if (fileName != common.UBOOT_DEFAULT_FILE_PATH):
                self.lineEdit_uboot.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_devtree_image_file(self):
        '''
        打开device_tree.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_dev_tree,"请选择device tree镜像文件"," ","dev tree files(*.img)")
        logging.debug("lj_select_devtree_image_file" + fileName)
        if fileName:
            if (fileName != common.DEVTREE_DEFAULT_FILE_PATH):
                self.lineEdit_dev_tree.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_otaloader_file(self):
        '''
        打开otaloader.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_otaloader,"请选择otaloader镜像文件"," ","otaloader files(*.img)")
        logging.debug("lj_select_otaloader_file" + fileName)
        if fileName:
            if (fileName != common.OTALOADER_DEFAULT_FILE_PATH):
                self.lineEdit_otaloader.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_splash_file(self):
        '''
        打开otaloader.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_splashr,"请选择splashr镜像文件"," ","splash files(*.dat)")
        logging.debug("lj_select_splash_file" + fileName)
        if fileName:
            if (fileName != common.SPLASH_DEFAULT_FILE_PATH):
                self.lineEdit_splash.setText(fileName)
            else:
                pass
        else:
            pass


    ###  for lj_flash_all
    def lj_flash_pmp_all(self,fileName):
        '''
        烧写pmp镜像
        :return:
        '''
        flag = False
        command = common.FLASH_PREFIX + common.PMP_ADDRESS + fileName
        logging.debug("\r\n")
        logging.debug("pmp command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        return flag

    def lj_flash_secboot_all(self,fileName):
        '''
        烧写secboot镜像
        :return:
        '''

        flag = False

        command = common.FLASH_PREFIX + common.SECBOOT_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("secboot command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        return flag

    def lj_flash_secos_all(self,fileName):
        '''
        烧写secos镜像
        :return:
        '''

        flag = False
        command = common.FLASH_PREFIX + common.SECOS_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("secos command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        return flag

    def lj_flash_uboot_all(self,fileName):
        '''
        烧写uboot镜像
        :return:
        '''
        flag_uboot = False
        flag_ubootbak = False
        command = common.FLASH_PREFIX + common.UBOOT_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("uboot command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag_uboot = True
                break
            else:
                flag_uboot = False

        # uboot_backup
        command_bak = common.FLASH_PREFIX + common.UBOOT_BACK_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("uboot backup command:" + command_bak)

        ret_bak = subprocess.Popen(command_bak,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret_bak.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag_ubootbak = True
                break
            else:
                flag_ubootbak = False

        ret.wait()

        return flag_uboot,flag_ubootbak

    def lj_flash_dev_tree_all(self,fileName):
        '''
        烧写device tree镜像
        :return:
        '''

        flag = False

        command = common.FLASH_PREFIX + common.DEVICETREE_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("device tree command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        return flag

    def lj_flash_otaloader_all(self,fileName):
        '''
        烧写otaloader镜像
        :return:
        '''

        flag = False

        command = common.FLASH_PREFIX + common.KERNELOTA_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("otaloader command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                ret.stdout.close()
                break
            else:
                flag = False
        ret.wait()

        return flag

    def lj_flash_splash_all(self,fileName):
        '''
        烧写splash镜像
        :return:
        '''

        flag = False

        command = common.FLASH_PREFIX + common.SPLASH_ADDRESS + " " + fileName
        logging.debug("\r\n")
        logging.debug("splash command all:" + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        ret.wait()

        return flag

    def lj_load_default_bbcb(self):
        self.lineEdit_manu_id.setText("21")
        self.lineEdit_hd_code.setText("4")
        self.lineEdit_loader_major.setText("3")
        self.lineEdit_loader_minor_2.setText("1")
        self.lineEdit_loader_type.setText("1")
        self.lineEdit_serial_number.setText("90021001")
        self.lineEdit_random_number.setText("80039001")

    def lj_flash_nvram_all(self):
        '''
        BBCB和FIXINFO在nvram分区，其它数据在ljinfo分区
        :return:
        '''

        logging.debug("\r\n")

        # 检查设备是否上线
        if showPlatform.OS_WIN:
            fp = open('toc\\nvram.bin',"rb+")
        else:
            fp = open('toc/nvram.bin',"rb+")

        #写入manufacturer id
        fp.seek(common.BBCB_OFFSET + 2,os.SEEK_SET)
        manufacturer_id = fp.read(1)
        manufacturer_id_new = int(self.lineEdit_manu_id.text())
        if(manufacturer_id != manufacturer_id_new):
            logging.debug("new manufacturer_id: " + str(manufacturer_id_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",manufacturer_id_new))
            fp.flush()

        # 写入hardware_code
        hardware_code = fp.read(1)
        hardware_code_new = int(self.lineEdit_hd_code.text())
        if(hardware_code != hardware_code_new):
            logging.debug("write new hardware_code: " + str(hardware_code_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",hardware_code_new))
            fp.flush()

        # 写入loader_major
        loader_major = fp.read(1)
        loader_major_new = int(self.lineEdit_loader_major.text())
        if(loader_major != loader_major_new):
            logging.debug("write new loader_major: " + str(loader_major_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_major_new))
            fp.flush()

        # 写入loader_minor
        loader_minor = fp.read(1)
        loader_minor_new = int(self.lineEdit_loader_minor_2.text())
        if(loader_minor != loader_minor_new):
            logging.debug("write new loader_minor: " + str(loader_minor_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_minor_new))
            fp.flush()

        # 写入loader_type
        loader_type = fp.read(1)
        loader_type_new = int(self.lineEdit_loader_type.text())
        if(loader_type != loader_type_new):
            logging.debug("write new loader_type: " + str(loader_type_new))
            fp.seek(-1,os.SEEK_CUR)
            fp.write(struct.pack("B",loader_type_new))
            fp.flush()

        # 写入serial_number
        serial_number = str(self.lineEdit_serial_number.text())
        logging.debug("input serial number: " + serial_number)

        # 以BCD码显示serial number
        fp.write(struct.pack("B",int(serial_number[0:2],16)))
        fp.write(struct.pack("B",int(serial_number[2:4],16)))
        fp.write(struct.pack("B",int(serial_number[4:6],16)))
        fp.write(struct.pack("B",int(serial_number[6:8],16)))
        fp.flush()

        # 写入random number
        random_number = str(self.lineEdit_random_number.text())
        if(len(random_number) == 0):
            random_number_new = str(lj_generate_random_number())
            logging.debug("generate random number: " + str(random_number_new))

            fp.write(struct.pack("B",int(random_number_new[0:2],16)))
            fp.write(struct.pack("B",int(random_number_new[2:4],16)))
            fp.write(struct.pack("B",int(random_number_new[4:6],16)))
            fp.write(struct.pack("B",int(random_number_new[6:8],16)))

        else:
            fp.write(struct.pack("B",int(random_number[0:2],16)))
            fp.write(struct.pack("B",int(random_number[2:4],16)))
            fp.write(struct.pack("B",int(random_number[4:6],16)))
            fp.write(struct.pack("B",int(random_number[6:8],16)))

        fp.flush()

        # 计算BBCB结构体的crc值并写入结构体中
        fp.seek(common.BBCB_OFFSET,os.SEEK_SET)
        bbcb = fp.read(common.BBCB_STRUCT_SIZE)
        crcCommand = "crc.exe "+ str(bbcb)

        crcRet = subprocess.Popen(crcCommand,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        crc_new = crcRet.stdout.read()
        logging.debug("crc:" + str(crc_new))

        fp.seek(common.BBCB_OFFSET,os.SEEK_SET)
        fp.write(struct.pack("2s",crc_new))
        fp.flush()

        fp.close()

        if showPlatform.OS_WIN:
            command = common.FLASH_PREFIX + common.NVRAM_ADDRESS + " toc\\nvram.bin"
        else:
            command = common.FLASH_PREFIX + common.NVRAM_ADDRESS + " toc/nvram.bin"

        logging.debug("nvram command: " + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)
            if str(line).count(common.BURN_ERROR_KEYWORD):
                flag = True
                break
            else:
                flag = False

        return flag

    def lj_flash_ljinfo(self):
        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.DEVICENOTONLINE)
            return

        if(common.FLAG_PMP_FLASHED == False):
            QtWidgets.QMessageBox.critical(self.button_flash_bbcb,common.BURNERROR,common.PMPISNOTFLASHED)
            return

    def lj_help_howto(self):
        '''
        打开软件使用帮助
        :return:
        '''

        QtWidgets.QMessageBox.information(self.menuBar,common.HOWTOUSE,common.HOWTOTEXT)

    def lj_help_about(self):
        '''
        显示软件相关信息
        :return:
        '''

        QMessageBox.aboutQt(self.menuBar,"PyQt5")

    def lj_reboot(self):
        '''
        重启设备
        :return:
        '''

        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_reboot,common.BURNERROR,common.DEVICENOTONLINE)
            return

        logging.debug("\r\n")
        ret = subprocess.Popen(common.FLASH_REBOOT,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)

    def lj_continue(self):
        '''
        继续启动设备
        :return:
        '''

        # 检查设备是否上线
        if(common.FLAG_DEVICE_ONLINE == False):
            QtWidgets.QMessageBox.critical(self.button_continue,common.BURNERROR,common.DEVICENOTONLINE)
            return

        logging.debug("\r\n")
        ret = subprocess.Popen(common.FLASH_CONTINUE,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.debug(line)

    def lj_select_pmp_image_file(self):
        '''
        打开pmp文件选择框
        :return:
        '''

        fileName,_ = QtWidgets.QFileDialog.getOpenFileName(self.lineEdit_pmp,"请选择pmp镜像文件"," ","pmp files(*.toc)")
        logging.debug("lj_select_pmp_image_file" + fileName)
        if fileName:
            if (fileName != common.PMP_DEFAULT_FILE_PATH):
                self.lineEdit_pmp.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_secboot_image_file(self):
        '''
        打开secboot文件选择框
        :return:
        '''

        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secboot,"请选择secboot镜像文件"," ","secboot files(*.toc)")
        logging.debug("lj_select_secboot_image_file" + fileName)
        if fileName:
            if (fileName != common.SECBOOT_DEFAULT_FILE_PATH):
                self.lineEdit_secboot.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_secos_image_file(self):
        '''
        打开secos文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_secos,"请选择secos镜像文件"," ","secos files(*.toc)")
        logging.debug("lj_select_secos_image_file" + fileName)
        if fileName:
            if (fileName != common.SECOS_DEFAULT_FILE_PATH):
                self.lineEdit_secos.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_uboot_image_file(self):
        '''
        打开uboot文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_uboot,"请选择uboot镜像文件"," ","uboot files(*.toc)")
        logging.debug("lj_select_uboot_image_file" + fileName)
        if fileName:
            if (fileName != common.UBOOT_DEFAULT_FILE_PATH):
                self.lineEdit_uboot.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_devtree_image_file(self):
        '''
        打开device_tree.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_dev_tree,"请选择device tree镜像文件"," ","dev tree files(*.img)")
        logging.debug("lj_select_devtree_image_file" + fileName)
        if fileName:
            if (fileName != common.DEVTREE_DEFAULT_FILE_PATH):
                self.lineEdit_dev_tree.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_otaloader_file(self):
        '''
        打开otaloader.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_otaloader,"请选择otaloader镜像文件"," ","otaloader files(*.img)")
        logging.debug("lj_select_otaloader_file" + fileName)
        if fileName:
            if (fileName != common.OTALOADER_DEFAULT_FILE_PATH):
                self.lineEdit_otaloader.setText(fileName)
            else:
                pass
        else:
            pass

    def lj_select_splash_file(self):
        '''
        打开otaloader.img文件选择框
        :return:
        '''
        logging.debug("\r\n")
        fileName,_ = QFileDialog.getOpenFileName(self.lineEdit_splashr,"请选择splashr镜像文件"," ","splash files(*.dat)")
        logging.debug("lj_select_splash_file" + fileName)
        if fileName:
            if (fileName != common.SPLASH_DEFAULT_FILE_PATH):
                self.lineEdit_splash.setText(fileName)
            else:
                pass
        else:
            pass
