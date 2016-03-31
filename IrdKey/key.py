# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import sys
import random
import logging
import struct
from ctypes import *

from common.constant import IRDETO_KEY_SIZE,IRDETO_CADATA_FILE,IRDETO_IRDETO_LIB_PATH,IRDETO_CRC_LIB_PATH
from common.constant import IRDETO_CUSTOM_KEY,IRDETO_DEVELOP_KEY

class IrdKeyOP(object):
    def __init__(self):
        pass

    @classmethod
    def getKey(self,path,serialNum,randomNum):
        flag = True

        buffer = create_string_buffer(IRDETO_KEY_SIZE + 2)

        keyHandle = cdll.LoadLibrary(IRDETO_IRDETO_LIB_PATH)
        func = keyHandle.lj_get_irdeto_key

        func.argtypes = (c_int,c_char_p,c_char_p,c_void_p)
        func.restype = c_int

        ret = func(IRDETO_CUSTOM_KEY,serialNum.encode('utf-8'),randomNum.encode('utf-8'),buffer)
        if ret == 0:
            crc = self.calcStrCRC(self,buffer=buffer[2:],size=IRDETO_KEY_SIZE)

            irdetoCrc, = struct.unpack('<h', bytes(buffer[0]+buffer[1]))

            if irdetoCrc == crc:
                print("crc ok.")
                logging.info("crc ok.")
                fp = open(path + '/' + IRDETO_CADATA_FILE,"wb")
                fp.write(buffer[2:])
                fp.close()
                flag = True
            else:
                print("crc wrong.")
                logging.error("crc wrong.")
                flag = False
        else:
            print('get IrdetoKey error.')
            logging.error('get IrdetoKey error.')
            flag = False

        return flag

    @classmethod
    def getRandomNumber(self):
        return str(random.randint(0,sys.maxsize))

    def calcStrCRC(self,buffer,size):
        handle = cdll.LoadLibrary(IRDETO_CRC_LIB_PATH)
        func = handle.LJ_nand_crc16

        func.argtypes = (c_void_p,c_int)
        func.restype = c_short

        crc = func(buffer,size)

        return crc