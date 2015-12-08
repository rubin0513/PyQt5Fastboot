# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow

from ui import *
import common

def initLogConfiguration():
    '''
    初始化日志配置
    '''
    logging.basicConfig(level = logging.DEBUG,
                        filename = common.LOGFILE,
                        filemode = 'a+',
                        format = '%(asctime)s - %(filename)s - line %(lineno)-4d - %(levelname)s - %(message)s',
                        datefmt = '%m-%d %H:%M')

if __name__ == '__main__':
    '''
    主函数
    '''
    initLogConfiguration()

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    ui.startDetectDevice()
    ui.lj_load_default_bbcb()

    sys.exit(app.exec_())