# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import logging

class PandaLog(object):
    def __init__(self):
        pass

    def initLogConfiguration(self,logFile):
        '''
        初始化日志配置
        '''
        logging.basicConfig(level = logging.DEBUG,
                            filename = logFile,
                            filemode = 'a+',
                            format = '%(asctime)s - %(filename)s - line %(lineno)-4d - %(levelname)s - %(message)s',
                            datefmt = '%m-%d %H:%M')