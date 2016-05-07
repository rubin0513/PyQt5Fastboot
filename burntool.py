# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import sys

from PyQt5.QtWidgets import QApplication

from ui.mainwindow import *
from log.log import *
from common.constant import LOGFILE

if __name__ == "__main__":
    PandaLog().initLogConfiguration(LOGFILE)

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
