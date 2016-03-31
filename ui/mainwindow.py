# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import logging
import shutil
from threading import Thread,active_count,RLock

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

from common.constant import STBTYPE
from common.constant import HOWTOUSE
from common.constant import HOWTOTEXT
from common.constant import CONFIGXML
from common.constant import ERRORTITLE
from common.constant import XMLNOTFOUND,IMAGEFILENOTFOUND
from common.constant import BURN_FIRST_ROUND_OK
from common.constant import SUCCESSTITLE
from common.constant import BURN_SECOND_ROUND_OK
from common.constant import FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE,FASTBOOT_ERROR_GET_SOCID,FASTBOOT_ERROR_CALC_CPCB,FASTBOOT_ERROR_GET_MAC
from common.constant import MYSQL_HOST,MYSQL_PORT,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DATABASE,MYSQL_TABLE,MYSQL_CONNECT_ERROR
from common.constant import CHECKSUM_ERROR,BURN_ERROR
from common.constant import FASTBOOT_ERROR_SECONDROUND_NEEDED,FASTBOOT_ERROR_FIRSTROUND_NEEDED,FASTBOOT_ERROR_UPDATE_SN
from common.constant import IRDETO_IRDETO_LIB_PATH,IRDETO_GET_KEY_ERROR,IRDETO_CADATA_FILE

from ui.ui_mainwindow import *
from burn.xml import *
from burn.fastboot import *
from sysinfo.generator import process_json
from db.mysql import *
from checksum.md5 import CalcMD5
from IrdKey.key import IrdKeyOP

class MainWindow(QMainWindow, Ui_MainWindow):

    checksumErrSignal = pyqtSignal(object)
    burnErrSignal = pyqtSignal(object)
    socIDErrSignal = pyqtSignal(object)
    cpcbErrSignal = pyqtSignal(object)
    getMacErrSignal = pyqtSignal(object)
    firstRoundNeededSignal = pyqtSignal(object)
    secondRoundNeededSignal = pyqtSignal(object)
    getMacErrSignal = pyqtSignal(object)
    updateMysqlErrSignal = pyqtSignal(object)
    imageNotFoundSignal = pyqtSignal(object)
    irdetoKeyErrSignal = pyqtSignal(object)
    mysqlConnectErrSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.close)

        self.actionCopy.triggered.connect(self.onCopyTriggered)
        self.actionPaste.triggered.connect(self.onPasteTriggered)
        self.actionCut.triggered.connect(self.onCutTriggered)

        self.actionHelp.triggered.connect(self.onHelpTriggered)
        self.actionAbout.triggered.connect(self.onAboutTriggered)

        self.firstRoundButton.clicked.connect(self.onFirstRoundClicked)
        self.secondRoundButton.clicked.connect(self.onSecondRoundClicked)

        self.firstRoundList = []
        self.secondRoundList = []
        self.onlineDevices = []

        self.firstRoundList,self.secondRoundList = self.parseXMLFile()

        print(self.firstRoundList)
        print(self.secondRoundList)
        logging.info(self.firstRoundList)
        logging.info(self.secondRoundList)

        self.burnFlag = False
        self.flag = True
        self.lock = RLock()

        self.checksumErrSignal.connect(self.slotShowMessage)
        self.burnErrSignal.connect(self.slotShowMessage)
        self.socIDErrSignal.connect(self.slotShowMessage)
        self.cpcbErrSignal.connect(self.slotShowMessage)
        self.getMacErrSignal.connect(self.slotShowMessage)
        self.firstRoundNeededSignal.connect(self.slotShowMessage)
        self.secondRoundNeededSignal.connect(self.slotShowMessage)
        self.getMacErrSignal.connect(self.slotShowMessage)
        self.updateMysqlErrSignal.connect(self.slotShowMessage)
        self.imageNotFoundSignal.connect(self.slotShowMessage)
        self.irdetoKeyErrSignal.connect(self.slotShowMessage)
        self.mysqlConnectErrSignal.connect(self.slotShowMessage)

    def onCopyTriggered(self):
        '''
        拷贝文本
        :return:
        '''
        pass

    def onPasteTriggered(self):
        '''
        粘贴文本
        :return:
        '''
        pass

    def onCutTriggered(self):
        '''
        剪切文本
        :return:
        '''
        pass

    def generateSysinfoImage(self,modifyDict):
        process_json(dict=modifyDict)

    def onHelpTriggered(self):
        QMessageBox.information(self.menubar,HOWTOUSE,HOWTOTEXT)

    def onAboutTriggered(self):
        '''
        显示软件信息
        :return:
        '''
        QMessageBox.aboutQt(self.menubar,"AboutQt")

    def parseXMLFile(self):
        if not os.path.exists(CONFIGXML):
            QMessageBox.critical(self.firstRoundButton,ERRORTITLE,XMLNOTFOUND)
            return
        else:
            xmlParse = XMLParser(CONFIGXML)
            return xmlParse.getTwoRoundTurple()

    def onFirstRoundClicked(self):
        self.flag = True
        fastboot = FastbootDevices()
        self.onlineDevices = fastboot.getOnLineDevices()
        if not self.onlineDevices:
            QMessageBox.critical(self.firstRoundButton,ERRORTITLE,FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE)
            return

        for i in range(len(self.onlineDevices)):
            t = Thread(target=self.firstRoundThreadTarget,args=(self.onlineDevices[i],))
            t.setDaemon(True)
            t.start()

        self.firstRoundButton.setCheckable(True)
        self.secondRoundButton.setCheckable(True)

        while True:
            if active_count() == 1:
                if self.flag:
                    print("FirstRound flash over.")
                    QMessageBox.information(self.firstRoundButton,SUCCESSTITLE,BURN_FIRST_ROUND_OK)
                else:
                    print("Firstround error occured.")
                break

    def onSecondRoundClicked(self):
        self.flag = True
        fastboot = FastbootDevices()
        self.onlineDevices.clear()
        self.onlineDevices = fastboot.getOnLineDevices()

        if not self.onlineDevices:
            QMessageBox.critical(self.secondRoundButton,ERRORTITLE,FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE)
            return

        for i in range(len(self.onlineDevices)):
            t = Thread(target=self.secondRoundThreadTarget,args=(self.onlineDevices[i],tuple(self.secondRoundList)))
            t.setDaemon(True)
            t.start()

        self.firstRoundButton.setCheckable(True)
        self.secondRoundButton.setCheckable(True)

        while True:
            if active_count() == 1:
                if self.flag:
                    QMessageBox.information(self.secondRoundButton,SUCCESSTITLE,BURN_SECOND_ROUND_OK)
                    print("SecondRound flash over.")
                else:
                    print("Secondround error occured.")
                break

    def firstRoundThreadTarget(self, device):
        print('FirstRoundThreadTarget' + device)
        self.firstRoundButton.setCheckable(False)
        self.secondRoundButton.setCheckable(False)

        # get socid
        temp,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if statusFlag:
            self.secondRoundNeededSignal.emit(FASTBOOT_ERROR_SECONDROUND_NEEDED)
            self.flag = False
            return

        for image in self.firstRoundList:
            print(image['name'])
            if not os.path.exists(image['path']):
                self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
                self.flag = False
                return

            if image['md5'] != CalcMD5().calcFileMd5(image['path']):
                self.checksumErrSignal.emit(CHECKSUM_ERROR)
                self.flag = False
                return

            self.burnFlag = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
            # if not self.burnFlag:
            #     logging.error('FirstRound flash error!' + image['name'])
            #     self.burnErrSignal.emit(BURN_ERROR)
            #     return

    def secondRoundThreadTarget(self,device,imageTurple):
        print('SecondRoundThreadTarget:' + device)

        self.firstRoundButton.setCheckable(False)
        self.secondRoundButton.setCheckable(False)

        dictionary = {}
        secondModifyList = []
        secondModifyList = list(imageTurple)

        # get socid
        socid,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if not statusFlag:
            self.firstRoundNeededSignal.emit(FASTBOOT_ERROR_FIRSTROUND_NEEDED)
            self.flag = False
            return

        if not len(socid):
            self.flag = False
            self.socIDErrSignal.emit(FASTBOOT_ERROR_GET_SOCID)
            return

        for image in secondModifyList:
            if not os.path.exists(image['path']):
                self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
                self.flag = False
                return

        # socidFormat = self.socIDFormatter(socid)
        socidFormat = str(socid)
        logging.info('\r\n')
        logging.info('socid: ' + socidFormat)

        # get serial number
        serialNumber = str(socidFormat[3:])
        logging.info('serial number: ' + serialNumber)

        # get mac
        mysql = MySQLCommand(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USERNAME,passwd=MYSQL_PASSWORD,db=MYSQL_DATABASE,table=MYSQL_TABLE)

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            self.flag = False
            return

        self.lock.acquire()
        mac = mysql.queryMysql(STBTYPE)
        if not mac:
            self.flag = False
            self.getMacErrSignal.emit(FASTBOOT_ERROR_GET_MAC)
            mysql.closeMysql()
            self.lock.release()
            return
        else:
            updateFlag = mysql.updateMysqlSN(mac=mac,sn=serialNumber)
            if not updateFlag:
                resetFlag = mysql.resetMysqlMACStatus(mac=mac)
                if not resetFlag:
                    print("update mac status failed.")
                    logging.error("update mac status failed.")

                print("Update mysql serialnum failed.")
                logging.error("Update mysql serialnum failed.")
                mysql.closeMysql()
                self.lock.release()
                self.flag = False
                self.updateMysqlErrSignal.emit(FASTBOOT_ERROR_UPDATE_SN)
                return

        mysql.closeMysql()
        self.lock.release()

        logging.info('\r\n')
        print(mac)
        logging.info(mac)

        randomNum = IrdKeyOP.getRandomNumber()
        print("random number:" + randomNum)
        logging.info("random number:" + randomNum)

        # generater sysinfo
        dictionary['STB_CA_KEY'] = str(socidFormat)
        dictionary['STB_ID'] = str(socidFormat)

        dictionary['STB_CHIP_ID'] = str(serialNumber)
        dictionary['IRDETO_SECURE_CHIP_SN'] = str(serialNumber)

        dictionary['STB_MAC'] = str(mac)

        dictionary['IRDETO_RANDOM_NUMBER'] = str(randomNum)

        self.generateSysinfoImage(dictionary)

        # get IrdetoKey
        irdetoKeyFlag = IrdKeyOP.getKey(path='soc' + socidFormat,serialNum=serialNumber,randomNum=randomNum)
        if not irdetoKeyFlag:
            self.flag = False
            self.irdetoKeyErrSignal.emit(IRDETO_GET_KEY_ERROR)

        dict_ro = {}
        dict_rw = {}
        dict_cadata = {}

        dict_ro['name'] = 'systeminfo_ro'
        dict_ro['address'] = 'systeminfo_ro'
        dict_ro['path'] = 'soc' + socidFormat + '/' + 'systeminfo_ro.img'
        dict_ro['md5'] = ''

        dict_rw['name'] = 'systeminfo_rw'
        dict_rw['address'] = 'systeminfo_rw'
        dict_rw['path'] = 'soc' + socidFormat + '/' + 'systeminfo_rw.img'
        dict_rw['md5'] = ''

        dict_cadata['name'] = 'cadata'
        dict_cadata['address'] = 'cadata'
        dict_cadata['path'] = 'soc' + socidFormat + '/' + IRDETO_CADATA_FILE
        dict_cadata['md5'] = ''

        if not dict_ro in secondModifyList:
            secondModifyList.append(dict_ro)

        if not dict_rw in secondModifyList:
            secondModifyList.append(dict_rw)

        if not dict_cadata in secondModifyList:
            secondModifyList.append(dict_cadata)

        print(secondModifyList)
        logging.info(secondModifyList)

        for image in secondModifyList:
            print(image['name'])
            if image['address'] != 'systeminfo_ro' and image['address'] != 'systeminfo_rw' and image['address'] != 'cadata':
                if image['md5'] != CalcMD5().calcFileMd5(image['path']):
                    self.flag = False
                    self.checksumErrSignal.emit(CHECKSUM_ERROR)
                    return

            self.burnFlag = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
            if not self.burnFlag:
                print('SecondRound flash error!' + image['name'])
                logging.error('SecondRound flash error!' + image['name'])
                self.flag = False
                self.burnErrSignal.emit(BURN_ERROR)
                return

        secondModifyList.remove(dict_ro)
        secondModifyList.remove(dict_rw)
        secondModifyList.remove(dict_cadata)

        # uboot cacl CPCB
        self.burnFlag = FastbootCalcCPCB.calcCPCB(deviceID=device)
        if not self.burnFlag:
            print('calc cpcb error.')
            logging.error('calc cpcb error.')
            self.flag = False
            self.cpcbErrSignal.emit(FASTBOOT_ERROR_CALC_CPCB)
            return

        self.deleteTocDir('soc' + socidFormat)

    def socIDFormatter(self,id):
        return ''.join(id.split('-'))

    def deleteTocDir(self,dirPath):
        try:
            shutil.rmtree(dirPath)
        except:
            print('Delete sysinfo toc failed.')
            logging.error("Delete sysinfo toc failed.")

    def slotShowMessage(self,message):
        QMessageBox.critical(self,ERRORTITLE,message)