# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui import *

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.setWindowIcon(QIcon('icon/lj.jpg'))
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.startDetectDevice()
    ui.lj_load_default_bbcb()
    sys.exit(app.exec_())