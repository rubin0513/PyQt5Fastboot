# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import subprocess
import logging
import time

from common.constant import FASTBOOT_CMD_DEVICES_PREFIX
from common.constant import FASTBOOT_CMD_FLASH_PREFIX
from common.constant import BURN_ERROR_KEYWORD
from common.constant import FASTBOOT_DEVICES_KEYWORD
from common.constant import FASTBOOT_CMD_SOCID_PREFIX
from common.constant import FASTBOOT_SOCID_KEYWORD
from common.constant import FASTBOOT_CMD_CALCCPCB_PREFIX
from common.constant import FASTBOOT_CPCB_KEYWORD
from common.constant import FASTBOOT_ERROR_TIMEOUT_IN_SECONDS

class FastbootDevices(object):
    def __init__(self):
        self.onLineDevices = []

    def getOnLineDevices(self):

        logging.info("\r\n")

        command = FASTBOOT_CMD_DEVICES_PREFIX
        logging.info("command: " + command)

        process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in process.stdout.readlines():
            if str(line).count(FASTBOOT_DEVICES_KEYWORD):
                index = str(line).find('usb')
                deviceID = str(line)[index:-3]
                logging.info("online devices:" + deviceID)
                self.onLineDevices.append(deviceID)

        process.wait()

        return self.onLineDevices


class FastbootSoCID(object):
    @classmethod
    def getSoCID(self,deviceID):
        '''

        :param deviceID:
        :return: status: True(Second Round)
                         False(First Round)
        '''

        socid = ''
        status = False
        deadline = time.time() + FASTBOOT_ERROR_TIMEOUT_IN_SECONDS

        command = FASTBOOT_CMD_SOCID_PREFIX + deviceID
        logging.info("command: " + command)

        process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in process.stdout.readlines():
            if str(line).count(FASTBOOT_SOCID_KEYWORD):
                socid = str(line)[9:-3]
                status = True
                break
            else:
                if time.time() > deadline:
                    socid = 0
                    return socid,status

        process.wait()

        return socid,status

class FastbootCalcCPCB(object):
    @classmethod
    def calcCPCB(self,deviceID):
        self.flag = False
        logging.info("\r\n")

        command = FASTBOOT_CMD_CALCCPCB_PREFIX + deviceID
        logging.info("command: " + command)

        process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in process.stdout.readlines():
            if str(line).count(FASTBOOT_CPCB_KEYWORD):
                self.flag = True

        process.wait()

        return self.flag

class FastbootFlash(object):
    def __init__(self):
        # self.deviceID = deviceID
        # self.imageAddress = imageAddress
        # self.imagePath = imagePath
        pass

    @classmethod
    def flashImage(self,deviceID,imageAddress,imagePath):
        flag = False
        logging.info("\r\n")

        command = FASTBOOT_CMD_FLASH_PREFIX + deviceID + " " + imageAddress + " " + imagePath
        logging.info(deviceID + " command: " + command)

        ret = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        for line in ret.stdout.readlines():
            logging.info(line)
            if str(line).count(BURN_ERROR_KEYWORD):
                flag = False
                break
            else:
                flag = True

        ret.wait()

        return flag

