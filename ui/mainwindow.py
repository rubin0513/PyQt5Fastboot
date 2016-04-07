# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import logging
import shutil
from threading import Thread,active_count,RLock

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal,QTimer

from common.constant import HOWTOUSE
from common.constant import HOWTOTEXT
from common.constant import CONFIGXML
from common.constant import ERRORTITLE
from common.constant import XMLNOTFOUND,IMAGEFILENOTFOUND
from common.constant import BURN_FIRST_ROUND_OK
from common.constant import SUCCESSTITLE
from common.constant import BURN_SECOND_ROUND_OK
from common.constant import FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE,FASTBOOT_ERROR_GET_SOCID,FASTBOOT_ERROR_CALC_CPCB,FASTBOOT_ERROR_GET_MAC
from common.constant import CHECKSUM_ERROR,BURN_ERROR
from common.constant import FASTBOOT_ERROR_SECONDROUND_NEEDED,FASTBOOT_ERROR_FIRSTROUND_NEEDED,FASTBOOT_ERROR_UPDATE_SN
from common.constant import IRDETO_IRDETO_LIB_PATH,IRDETO_GET_KEY_ERROR,IRDETO_CADATA_FILE
from common.constant import PRINTER_OK_MSG,PRINTER_BURN_NEEDED_MSG
from common.constant import FASTBOOT_ERROR_GET_SERIALNUMBER,PRINTER_ERROR_MSG
from common.constant import FASTBOOT_SHOW_DEVICES_COUNT_TIMEOUT
from common.constant import CONFIGSYSXML,SYSXMLNOTFOUND
from common.constant import MYSQL_CONNECT_ERROR
from common.constant import SYSINFOJSONFILE

from ui.ui_mainwindow import *
from burn.xml import *
from burn.fastboot import *
from sysinfo.generator import process_json
from db.mysql import *
from checksum.md5 import CalcMD5
from IrdKey.key import IrdKeyOP
from printer.print import *

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
    burnNeededSignal = pyqtSignal(object)
    getSnErrSignal = pyqtSignal(object)
    printMACSNErrSignal = pyqtSignal(object)

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
        self.printButton.clicked.connect(self.onPrinterClicked)

        self.firstRoundList = []
        self.secondRoundList = []
        self.sysXMLDict = {}
        self.onlineDevices = []

        self.firstRoundList,self.secondRoundList = self.parseXMLFile(CONFIGXML)
        self.sysXMLDict = self.parseSYSXMLFile(CONFIGSYSXML)
        logging.info(self.sysXMLDict)
        print('burnTool version:')
        print(self.sysXMLDict['version'])

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
        self.updateMysqlErrSignal.connect(self.slotShowMessage)
        self.imageNotFoundSignal.connect(self.slotShowMessage)
        self.irdetoKeyErrSignal.connect(self.slotShowMessage)
        self.mysqlConnectErrSignal.connect(self.slotShowMessage)
        self.burnNeededSignal.connect(self.slotShowMessage)
        self.getSnErrSignal.connect(self.slotShowMessage)
        self.printMACSNErrSignal.connect(self.slotShowMessage)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showCurrentDevices)
        self.startCount()

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
        process_json(jsonFile=SYSINFOJSONFILE,dict=modifyDict)

    def onHelpTriggered(self):
        versionMsg = self.sysXMLDict['version']
        QMessageBox.information(self.menubar,HOWTOUSE,HOWTOTEXT + '4、当前版本v' + versionMsg)

    def onAboutTriggered(self):
        '''
        显示软件信息
        :return:
        '''
        QMessageBox.aboutQt(self.menubar,"AboutQt")

    def parseXMLFile(self,path):

        if not os.path.exists(path):
            QMessageBox.critical(self.firstRoundButton,ERRORTITLE,XMLNOTFOUND)
            return
        else:
            xmlParse = XMLParser(CONFIGXML)
            return xmlParse.getTwoRoundTurple()

    def parseSYSXMLFile(self,path):
        if not os.path.exists(path):
            QMessageBox.critical(self.firstRoundButton,ERRORTITLE,SYSXMLNOTFOUND)
            return
        else:
            sysXMLParse = SYSXMLParser(CONFIGSYSXML)
            return sysXMLParse.getSysXMLDict()

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

    def onPrinterClicked(self):
        self.flag = True
        fastboot = FastbootDevices()
        self.onlineDevices.clear()
        self.onlineDevices = fastboot.getOnLineDevices()

        if not self.onlineDevices:
            QMessageBox.critical(self.secondRoundButton,ERRORTITLE,FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE)
            return

        for i in range(len(self.onlineDevices)):
            t = Thread(target=self.printerThreadTarget,args=(self.onlineDevices[i],))
            t.setDaemon(True)
            t.start()

        while True:
            if active_count() == 1:
                if self.flag:
                    QMessageBox.information(self.printButton,SUCCESSTITLE,PRINTER_OK_MSG)
                    print("Printer over.")
                else:
                    print("Printer error occured.")
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
            FastbootLampCommand.setRedOn(deviceID=device)
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
                FastbootLampCommand.setRedOn(deviceID=device)
                return

            self.burnFlag = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
            if not self.burnFlag:
                print('FirstRound flash error first!' + image['name'])
                logging.error('FirstRound flash error first!' + image['name'])
                flagAgain = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
                if not flagAgain:
                    print('FirstRound flash error secondly!' + image['name'])
                    logging.error('FirstRound flash error secondly!' + image['name'])
                    self.burnErrSignal.emit(BURN_ERROR)
                    return

    def secondRoundThreadTarget(self,device,imageTurple):
        print('SecondRoundThreadTarget:' + device)
        FastbootLampCommand.setRedFast(deviceID=device)

        self.firstRoundButton.setCheckable(False)
        self.secondRoundButton.setCheckable(False)

        dictionary = {}
        secondModifyList = []
        secondModifyList = list(imageTurple)

        # 不带冒号MAC
        macAddr0 = ''

        # get socid
        socid,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if not statusFlag:
            self.firstRoundNeededSignal.emit(FASTBOOT_ERROR_FIRSTROUND_NEEDED)
            self.flag = False
            return

        if not len(socid):
            self.flag = False
            self.socIDErrSignal.emit(FASTBOOT_ERROR_GET_SOCID)
            FastbootLampCommand.setRedOn(deviceID=device)
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

        mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'],port=int(self.sysXMLDict['mysqlport']),user=self.sysXMLDict['mysqluser'],\
                             passwd=self.sysXMLDict['mysqlpassword'],db=self.sysXMLDict['mysqldatabase'],table=self.sysXMLDict['mysqltable'])
        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            FastbootLampCommand.setRedOn(deviceID=device)
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            self.flag = False
            return

        self.lock.acquire()
        snExistFlag = mysql.queryMysqlSN(sn=socidFormat)
        if not snExistFlag:
            # 序列号不在数据库中，重新获取MAC，更新序列号
            mac = mysql.queryMysql(self.sysXMLDict['mysqlstbtype'])
            print('get mac from db:')
            print(mac)
            logging.info('get mac from db=')
            logging.info(mac)

            if not mac:
                self.flag = False
                self.getMacErrSignal.emit(FASTBOOT_ERROR_GET_MAC)
                mysql.closeMysql()
                self.lock.release()
                FastbootLampCommand.setRedOn(deviceID=device)
                return
            else:
                macAddr0 = mac
                updateFlag = mysql.updateMysqlSN(mac=mac,sn=socidFormat)
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
                    FastbootLampCommand.setRedOn(deviceID=device)
                    return
                else:
                    dictionary['STB_MAC'] = str(macAddr0[0:2] + ':' + macAddr0[2:4] + ':' + macAddr0[4:6] + ':' + macAddr0[6:8] + ':' + macAddr0[8:10] + ':' + macAddr0[10:12])

        else:
            # 已经是烧录过的盒子，使用已有MAC,macFormat带冒号
            macFormat = FastbootMACCommand.getMAC(deviceID=device)
            dictionary['STB_MAC'] = str(macFormat)
            print('burned stb MAC:')
            print(macFormat)
            logging.info('burned stb MAC=')
            logging.info(macFormat)

        mysql.closeMysql()
        self.lock.release()

        logging.info('\r\n')

        randomNum = IrdKeyOP.getRandomNumber()
        print("random number:" + randomNum)
        logging.info("random number:" + randomNum)

        # generater sysinfo
        dictionary['STB_CA_KEY'] = str(socidFormat)
        dictionary['STB_ID'] = str(socidFormat)
        dictionary['STB_CHIP_ID'] = str(socidFormat)
        dictionary['IRDETO_SECURE_CHIP_SN'] = str(serialNumber)
        dictionary['IRDETO_RANDOM_NUMBER'] = str(randomNum)

        self.generateSysinfoImage(dictionary)

        # get IrdetoKey
        irdetoKeyFlag = IrdKeyOP.getKey(path='soc' + socidFormat,serialNum=serialNumber,randomNum=randomNum,keyType=int(self.sysXMLDict['irdetokeytype']))
        if not irdetoKeyFlag:
            self.flag = False
            self.irdetoKeyErrSignal.emit(IRDETO_GET_KEY_ERROR)
            FastbootLampCommand.setRedOn(deviceID=device)
            return

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
                    FastbootLampCommand.setRedOn(deviceID=device)
                    return

            self.burnFlag = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
            if not self.burnFlag:
                print('SecondRound flash error!' + image['name'])
                logging.error('SecondRound flash error!' + image['name'])
                self.flag = False
                self.burnErrSignal.emit(BURN_ERROR)
                FastbootLampCommand.setRedOn(deviceID=device)
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
            FastbootLampCommand.setRedOn(deviceID=device)
            return

        self.deleteTocDir('soc' + socidFormat)
        FastbootLampCommand.setGreenOn(deviceID=device)

    def printerThreadTarget(self,device):
        print('FirstRoundThreadTarget' + device)
        self.firstRoundButton.setCheckable(False)
        self.secondRoundButton.setCheckable(False)
        self.printButton.setCheckable(False)

        # get mac
        macAddr0 = FastbootMACCommand().getMAC(deviceID=device)
        print(macAddr0)
        if len(macAddr0) == 0:
            self.burnNeededSignal.emit(PRINTER_BURN_NEEDED_MSG)
            self.flag = False
            return

        mac = ''.join(macAddr0.split(':'))
        print(mac)

        mysql = MySQLCommand(host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USERNAME,passwd=MYSQL_PASSWORD,db=MYSQL_DATABASE,table=MYSQL_TABLE)

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            FastbootLampCommand.setRedOn(deviceID=device)
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            self.flag = False
            return

        self.lock.acquire()
        sn = mysql.queryMysqlSNByMAC(mac=mac)
        if not sn:
            self.flag = False
            self.getSnErrSignal.emit(FASTBOOT_ERROR_GET_SERIALNUMBER)
            mysql.closeMysql()
            self.lock.release()
            FastbootLampCommand.setRedOn(deviceID=device)
            return
        else:
            printFlag = MacSNPrint.sendInfoToPrinter(host=self.sysXMLDict['printerhost'],port=self.sysXMLDict['printerport'],sn=sn,mac=mac)
            if not printFlag:
                self.printMACSNErrSignal.emit(PRINTER_ERROR_MSG)
                FastbootLampCommand.setRedOn(deviceID=device)
            else:
                FastbootLampCommand.setGreenOn(deviceID=device)

        mysql.closeMysql()
        self.lock.release()

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

    def showCurrentDevices(self):
        curDevices = []
        curDevices = FastbootShowDevices.getOnLineDevices()
        print(curDevices)
        logging.info(curDevices)
        self.label_count.setText(str(len(curDevices)))

    def startCount(self):
        self.timer.start(FASTBOOT_SHOW_DEVICES_COUNT_TIMEOUT)

