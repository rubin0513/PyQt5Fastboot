# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import time

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

from fastboot import lj_list_device_id

class detectDeviceThread(QThread):

    detectSignal = pyqtSignal(object)

    def __int__(self):
        QThread.__init__(self)

    def run(self):
        while True:
            deviceNum = lj_list_device_id(self)
            self.detectSignal.emit(deviceNum)
            time.sleep(2)