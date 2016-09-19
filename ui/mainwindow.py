# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import logging
import shutil
from threading import Thread,active_count,RLock

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow,QInputDialog,QLineEdit
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
from common.constant import PRINTER_OK_MSG,PRINTER_BURN_NEEDED_MSG,PRINTER_SN_NOT_EQUAL_TO_DB
from common.constant import FASTBOOT_ERROR_GET_SERIALNUMBER,PRINTER_ERROR_MSG
from common.constant import FASTBOOT_SHOW_DEVICES_COUNT_TIMEOUT,MYSQL_SHOW_AVAILABLE_MAC_COUNT_TIMEOUT
from common.constant import CONFIGSYSXML,SYSXMLNOTFOUND
from common.constant import MYSQL_CONNECT_ERROR,MYSQL_BACKUP_SUCCESS,MYSQL_BACKUP_FAILED,MYSQL_INFO_BACKUP
from common.constant import SYSINFOJSONFILE,FASTBOOT_ERROR_NOT_INSTALLED,MYSQL_ERROR_DUMP_NOT_INSTALLED
from common.constant import PO_INPUTDIALOG_INFO,PO_INPUTDIALOG_TITLE,PO_INPUTDIALOG_PONUMBER_HINT
from common.constant import RESET_MAC_SUCCESS,RESET_MAC_FAILED,RESET_MAC_INFO,FASTBOOT_ERROR_RESET_MAC_STATUS

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
    printSNNotEqualInDBSignal = pyqtSignal(object)
    secondThreadEndSignal = pyqtSignal(object)
    firstThreadEndSignal = pyqtSignal(object)
    printThreadEndSignal = pyqtSignal(object)
    resetMysqlErrSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.checkFastbootTool()

        self.actionExit.triggered.connect(self.close)

        self.actionCopy.triggered.connect(self.onCopyTriggered)
        self.actionPaste.triggered.connect(self.onPasteTriggered)
        self.actionCut.triggered.connect(self.onCutTriggered)

        self.actionHelp.triggered.connect(self.onHelpTriggered)
        self.actionAbout.triggered.connect(self.onAboutTriggered)
        # self.action_backupDB.triggered.connect(self.onBackupDBTriggered)
        # self.action_reset_mac.triggered.connect(self.onResetMACTriggered)

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

        self.firstPhaseCount = 0
        self.firstPhaseErrCount = 0

        self.secondPhaseCount = 0
        self.secondPhaseErrCount = 0

        self.printPhaseCount = 0
        self.printPhaseErrCount = 0

        self.poNumber = ''
        self.showPONInputDialog()

        self.burnFlag = False
        self.lock = RLock()

        self.checksumErrSignal.connect(self.slotShowMessage)
        self.burnErrSignal.connect(self.slotShowMessage)
        self.socIDErrSignal.connect(self.slotShowMessage)
        self.cpcbErrSignal.connect(self.slotShowMessage)
        self.getMacErrSignal.connect(self.slotShowMessage)
        self.firstRoundNeededSignal.connect(self.slotShowMessage)
        self.secondRoundNeededSignal.connect(self.slotShowMessage)
        self.updateMysqlErrSignal.connect(self.slotShowMessage)
        self.resetMysqlErrSignal.connect(self.slotShowMessage)
        self.imageNotFoundSignal.connect(self.slotShowMessage)
        self.irdetoKeyErrSignal.connect(self.slotShowMessage)
        self.mysqlConnectErrSignal.connect(self.slotShowMessage)
        self.burnNeededSignal.connect(self.slotShowMessage)
        self.getSnErrSignal.connect(self.slotShowMessage)
        self.printMACSNErrSignal.connect(self.slotShowMessage)
        self.printSNNotEqualInDBSignal.connect(self.slotShowMessage)
        self.secondThreadEndSignal.connect(self.secondSlotThreadOver)
        self.firstThreadEndSignal.connect(self.firstSlotThreadOver)
        self.printThreadEndSignal.connect(self.printSlotThreadOver)

        self.timerDevice = QTimer(self)
        self.timerMAC = QTimer(self)
        self.timerDevice.timeout.connect(self.showCurrentDevices)

        if(self.sysXMLDict['isNeedToConnectMysql'] == 'yes'):
            self.timerMAC.timeout.connect(self.showCurrentAvailableMAC)
            self.timerMAC.start(MYSQL_SHOW_AVAILABLE_MAC_COUNT_TIMEOUT)
        elif(self.sysXMLDict['isNeedToConnectMysql'] == 'no'):
            pass

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

        QMessageBox.information(self.menubar,HOWTOUSE,HOWTOTEXT)

    def onAboutTriggered(self):
        '''
        显示软件信息
        :return:
        '''

        versionMsg = self.sysXMLDict['version']
        QMessageBox.about(self.menubar,'软件信息','版本v' + versionMsg)

    def onBackupDBTriggered(self):

        self.checkMysqldumpTool()

        backupFlag = True
        fileName,okPressed = QInputDialog.getText(self,"数据库备份","请输入文件名:",QLineEdit.Normal, "dbback.sql")
        if okPressed and fileName.strip():
            print('DBBackupFile:' + fileName)
            logging.info('DBBackupFile:' + fileName)

            logging.info("\r\n")

            command = 'mysqldump -u' + self.sysXMLDict['mysqluser'] + ' -h ' + self.sysXMLDict['mysqlhost'] + ' -p' + self.sysXMLDict['mysqlpassword'] \
                        + ' ' + self.sysXMLDict['mysqldatabase'] + ' ' + self.sysXMLDict['mysqltable'] + '>' + fileName
            print(command)
            logging.info("Backup DB command: " + command)

            process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            for line in process.stdout.readlines():
                if str(line).count('error'):
                    backupFlag = False
                    break

            process.wait()

            if backupFlag:
                QMessageBox.information(self,SUCCESSTITLE,MYSQL_BACKUP_SUCCESS)
            else:
                QMessageBox.critical(self,ERRORTITLE,MYSQL_BACKUP_FAILED)

        else:
            QMessageBox.critical(self,ERRORTITLE,MYSQL_INFO_BACKUP)

    def onResetMACTriggered(self):
        resetFlag = False
        mac,okPressed = QInputDialog.getText(self,"MAC状态重置","请输入MAC号:",QLineEdit.Normal, " ")
        if okPressed and mac.strip():
            print('mac:' + mac)
            logging.info('mac:' + mac)
            logging.info("\r\n")

            mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'],port=int(self.sysXMLDict['mysqlport']),user=self.sysXMLDict['mysqluser'],\
                             passwd=self.sysXMLDict['mysqlpassword'],db=self.sysXMLDict['mysqldatabase'],table=self.sysXMLDict['mysqltable'])
            mysqlConFlag = mysql.connectMysql()
            if not mysqlConFlag:
                self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
                return

            self.lock.acquire()
            resetFlag = mysql.resetMysqlMACStatusAndSN(mac=mac,stbType=self.sysXMLDict['mysqlstbtype'],poNumber=self.poNumber)
            if resetFlag:
                QMessageBox.information(self,SUCCESSTITLE,RESET_MAC_SUCCESS)
            else:
                QMessageBox.critical(self,ERRORTITLE,RESET_MAC_FAILED)

            self.lock.release()
            mysql.closeMysql()

        else:
            QMessageBox.critical(self,ERRORTITLE,RESET_MAC_INFO)

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
        self.firstPhaseErrCount = 0
        self.firstPhaseCount = 0

        if not len(self.firstRoundList):
	        self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
	        return

        fastboot = FastbootDevices()
        self.onlineDevices = fastboot.getOnLineDevices()
        if not self.onlineDevices:
            QMessageBox.critical(self.firstRoundButton,ERRORTITLE,FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE)
            return

        for i in range(len(self.onlineDevices)):
            t = Thread(target=self.firstRoundThreadTarget,args=(self.onlineDevices[i],))
            t.setDaemon(True)
            t.start()

    def firstSlotThreadOver(self, flag):
        print('First Thread Over flag:', flag)
        logging.info('First Thread Over flag:' + str(flag))
        self.firstPhaseCount += 1

        if not flag:
            self.firstPhaseErrCount += 1

        if self.firstPhaseCount == len(self.onlineDevices):
            if self.firstPhaseErrCount == 0:
                QMessageBox.information(self.firstRoundButton, SUCCESSTITLE, BURN_FIRST_ROUND_OK)
                logging.info("FirstRound flash over.")
            else:
                QMessageBox.critical(self.firstRoundButton,ERRORTITLE,self.firstPhaseErrCount + "pecs" + BURN_ERROR)

    def onSecondRoundClicked(self):
        self.secondPhaseCount = 0
        self.secondPhaseErrCount = 0

        if not len(self.secondRoundList):
	        self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
	        return

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

    def secondSlotThreadOver(self, flag):
        print('Second Thread Over flag:', flag)
        logging.info('Second Thread Over flag:' + str(flag))
        self.secondPhaseCount += 1

        if not flag:
            self.secondPhaseErrCount += 1

        if self.secondPhaseCount == len(self.onlineDevices):
            if self.secondPhaseErrCount == 0:
                QMessageBox.information(self.secondRoundButton, SUCCESSTITLE, BURN_SECOND_ROUND_OK)
                logging.info("SecondRound flash over.")
            else:
                QMessageBox.critical(self.secondRoundButton, ERRORTITLE, self.secondPhaseErrCount + "pecs" + BURN_ERROR)
                logging.error("SecondRound flash over error.")

    def onPrinterClicked(self):
        self.printPhaseCount = 0
        self.printPhaseErrCount = 0

        fastboot = FastbootDevices()
        self.onlineDevices.clear()
        self.onlineDevices = fastboot.getOnLineDevices()

        if not self.onlineDevices:
            QMessageBox.critical(self.printButton,ERRORTITLE,FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE)
            return

        for i in range(len(self.onlineDevices)):
            t = Thread(target=self.printerThreadTarget,args=(self.onlineDevices[i],))
            t.setDaemon(True)
            t.start()

    def printSlotThreadOver(self, flag):
        print('Print Thread Over flag:', flag)
        logging.info('Print Thread Over flag:' + str(flag))
        self.printPhaseCount += 1

        if not flag:
            self.printPhaseErrCount += 1

        if self.printPhaseCount == len(self.onlineDevices):
            if self.printPhaseErrCount == 0:
                QMessageBox.information(self.printButton, SUCCESSTITLE, PRINTER_OK_MSG)
                print("Print over.")
            else:
                QMessageBox.critical(self.printButton, ERRORTITLE, self.printPhaseErrCount + "pecs" + BURN_ERROR)

    def firstRoundThreadTarget(self, device):
        print('FirstRoundThreadTarget' + device)

        # get socid
        temp,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if statusFlag:
            self.secondRoundNeededSignal.emit(FASTBOOT_ERROR_SECONDROUND_NEEDED)
            FastbootLampCommand.setRedOn(deviceID=device)
            return

        for image in self.firstRoundList:
            logging.info(image['name'])
            if not os.path.exists(image['path']):
                self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
                return

            if image['md5'] != CalcMD5().calcFileMd5(image['path']):
                self.checksumErrSignal.emit(CHECKSUM_ERROR)
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
                    FastbootLampCommand.setRedOn(deviceID=device)
                    return

        self.firstThreadEndSignal.emit(True)

    def secondRoundThreadTarget(self,device,imageTurple):
        print('SecondRoundThreadTarget:' + device)
        FastbootLampCommand.setRedFast(deviceID=device)
        needCalcCPCBFlag = False

        dictionary = {}
        secondModifyList = []
        secondModifyList = list(imageTurple)

        # 不带冒号MAC
        macAddr0 = ''

        # get socid
        socid,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if not statusFlag:
            self.firstRoundNeededSignal.emit(FASTBOOT_ERROR_FIRSTROUND_NEEDED)
            return

        if not len(socid):
            self.socIDErrSignal.emit(FASTBOOT_ERROR_GET_SOCID)
            FastbootLampCommand.setRedOn(deviceID=device)
            return

        for image in secondModifyList:
            if not os.path.exists(image['path']):
                self.imageNotFoundSignal.emit(IMAGEFILENOTFOUND)
                return

            if image['address'] == 'iploader':
                needCalcCPCBFlag = True

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
            return

        self.lock.acquire()
        macFormat = FastbootMACCommand.getMAC(deviceID=device)
        logging.info('local mac:' + str(macFormat))
        print('local mac:',macFormat)

        snExistFlag = mysql.queryMysqlSN(sn=socidFormat,mac=self.macFormatter(macFormat),stbType=self.sysXMLDict['mysqlstbtype'],poNumber=self.poNumber)
        if not snExistFlag:
            # 序列号 and mac不在数据库中
            mac = mysql.queryMysql(stbType=self.sysXMLDict['mysqlstbtype'],poNumber=self.poNumber)
            print('get mac from db=',mac)
            logging.info('get mac from db=' + str(mac))

            if not mac:
                self.getMacErrSignal.emit(FASTBOOT_ERROR_GET_MAC)
                mysql.closeMysql()
                self.lock.release()
                FastbootLampCommand.setRedOn(deviceID=device)
                return
            else:
                macAddr0 = mac
                updateFlag = mysql.updateMysqlSN(mac=mac,sn=socidFormat,stbType=self.sysXMLDict['mysqlstbtype'],poNumber=self.poNumber)
                if not updateFlag:
                    print("Update mysql serialnum failed.")
                    logging.error("Update mysql serialnum failed.")
                    mysql.closeMysql()
                    self.lock.release()
                    self.updateMysqlErrSignal.emit(FASTBOOT_ERROR_RESET_MAC_STATUS)
                    FastbootLampCommand.setRedOn(deviceID=device)
                    self.resetMysqlMACStatus(mac=mac)
                    return
                else:
                    dictionary['STB_MAC'] = str(macAddr0[0:2] + ':' + macAddr0[2:4] + ':' + macAddr0[4:6] + ':' + macAddr0[6:8] + ':' + macAddr0[8:10] + ':' + macAddr0[10:12])

        else:
            # 已经是烧录过的盒子，使用已有MAC,macFormat带冒号
            # macFormat = FastbootMACCommand.getMAC(deviceID=device)
            dictionary['STB_MAC'] = str(macFormat)
            print('burned stb MAC=')
            print(macFormat)
            logging.info('burned stb MAC=')
            logging.info(macFormat)

        mysql.closeMysql()
        self.lock.release()

        randomNum = IrdKeyOP.getRandomNumber()
        # print("random number:" + randomNum)
        logging.info("random number:" + randomNum)

        dictionary['BOOT_METHOD'] = 'normal'
        # 检查包中是否有factorytest.img镜像
        for imgList in secondModifyList:
            if imgList['name'] == 'factorytest.img' and imgList['address'] == 'otaloaderbak':
                dictionary['BOOT_METHOD'] = '0x98'
                break

        # generater sysinfo
        dictionary['STB_CA_KEY'] = str(socidFormat)
        dictionary['STB_ID'] = str(socidFormat)
        dictionary['IRDETO_SECURE_CHIP_SN'] = str(serialNumber)
        dictionary['IRDETO_RANDOM_NUMBER'] = str(randomNum)

        self.generateSysinfoImage(dictionary)

        # get IrdetoKey
        irdetoKeyFlag = IrdKeyOP.getKey(path='soc' + socidFormat,serialNum=serialNumber,randomNum=randomNum,keyType=int(self.sysXMLDict['irdetokeytype']))
        if not irdetoKeyFlag:
            self.irdetoKeyErrSignal.emit(IRDETO_GET_KEY_ERROR)
            FastbootLampCommand.setRedOn(deviceID=device)
            self.resetMysqlMACAndSN(mac=self.macFormatter(dictionary['STB_MAC']))
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

        if not dict_rw in secondModifyList:
            secondModifyList.append(dict_rw)

        if not dict_cadata in secondModifyList:
            secondModifyList.append(dict_cadata)

        if not dict_ro in secondModifyList:
            secondModifyList.append(dict_ro)

        print(secondModifyList)
        logging.info(secondModifyList)

        for image in secondModifyList:
            logging.info(image['name'])
            if image['address'] != 'systeminfo_ro' and image['address'] != 'systeminfo_rw' and image['address'] != 'cadata':
                if image['md5'] != CalcMD5().calcFileMd5(image['path']):
                    self.checksumErrSignal.emit(CHECKSUM_ERROR)
                    FastbootLampCommand.setRedOn(deviceID=device)
                    secondModifyList.remove(dict_ro)
                    secondModifyList.remove(dict_rw)
                    self.deleteTocDir('soc' + socidFormat)
                    self.resetMysqlMACAndSN(mac=self.macFormatter(dictionary['STB_MAC']))
                    return

            self.burnFlag = FastbootFlash().flashImage(deviceID=device, imageAddress=image['address'],imagePath=image['path'])
            if not self.burnFlag:
                print('SecondRound flash error!' + image['name'] + 'soc:' + socidFormat)
                logging.error('SecondRound flash error!' + image['name'] + 'soc:' + socidFormat)
                self.burnErrSignal.emit(BURN_ERROR)
                FastbootLampCommand.setRedOn(deviceID=device)
                secondModifyList.remove(dict_ro)
                secondModifyList.remove(dict_rw)
                self.deleteTocDir('soc' + socidFormat)
                self.resetMysqlMACAndSN(mac=self.macFormatter(dictionary['STB_MAC']))
                if not FastbootFlash.erasePartition(deviceID=device, partition='systeminfo_ro'):
                    print('erase systeminfo_ro failed.')
                    logging.error('erase systeminfo_ro failed.')
                return

        if dict_ro in secondModifyList:
            secondModifyList.remove(dict_ro)
		
        if dict_rw in secondModifyList:
            secondModifyList.remove(dict_rw)
			
        if dict_cadata in secondModifyList:
            secondModifyList.remove(dict_cadata)

        self.deleteTocDir('soc' + socidFormat)

        # uboot cacl CPCB
        if needCalcCPCBFlag:
            print('start to calc cpcb.')
            logging.info('start to cacl cpcb.')
            self.burnFlag = FastbootCalcCPCB.calcCPCB(deviceID=device)
            if not self.burnFlag:
                print('calc cpcb error.')
                logging.error('calc cpcb error.')
                self.cpcbErrSignal.emit(FASTBOOT_ERROR_CALC_CPCB)
                FastbootLampCommand.setRedOn(deviceID=device)
                self.resetMysqlMACAndSN(mac=self.macFormatter(dictionary['STB_MAC']))
                if not FastbootFlash.erasePartition(deviceID=device, partition='systeminfo_ro'):
                    print('erase systeminfo_ro failed.')
                    logging.error('erase systeminfo_ro failed.')
                return

        FastbootLampCommand.setGreenOn(deviceID=device)
        self.secondThreadEndSignal.emit(True)

    def resetMysqlMACStatus(self,mac):
        mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'], port=int(self.sysXMLDict['mysqlport']),
                             user=self.sysXMLDict['mysqluser'], passwd=self.sysXMLDict['mysqlpassword'],
                             db=self.sysXMLDict['mysqldatabase'], table=self.sysXMLDict['mysqltable'])

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            logging.info('reset status connect failed.')
            return False

        locker = RLock()
        locker.acquire()

        resetFlag = mysql.resetMysqlMACStatus(mac=mac,stbType=self.sysXMLDict['mysqlstbtype'], poNumber=self.poNumber)
        if resetFlag:
            logging.info('reset mysql status success.')
        else:
            logging.info('reset mysql status failed.')
            mysql.closeMysql()
            locker.release()
            return False

        mysql.closeMysql()
        locker.release()

        return True

    def resetMysqlMACAndSN(self,mac):
        mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'], port=int(self.sysXMLDict['mysqlport']),
                             user=self.sysXMLDict['mysqluser'], passwd=self.sysXMLDict['mysqlpassword'],
                             db=self.sysXMLDict['mysqldatabase'], table=self.sysXMLDict['mysqltable'])

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            logging.info('reset status connect failed.')
            return False

        locker = RLock()
        locker.acquire()

        resetFlag = mysql.resetMysqlMACStatusAndSN(mac=mac,stbType=self.sysXMLDict['mysqlstbtype'], poNumber=self.poNumber)
        if resetFlag:
            logging.info('reset mysql status success.')
        else:
            logging.info('reset mysql status failed.')
            mysql.closeMysql()
            locker.release()
            return False

        mysql.closeMysql()
        locker.release()

        return True

    def printerThreadTarget(self,device):
        print('printerThreadTarget' + device)

        # get mac
        macAddr0 = FastbootMACCommand().getMAC(deviceID=device)
        logging.info(macAddr0)
        if len(macAddr0) == 0:
            self.burnNeededSignal.emit(PRINTER_BURN_NEEDED_MSG)
            return

        mac = ''.join(macAddr0.split(':'))
        print(mac)

        # get sn
        sn,statusFlag = FastbootSoCID().getSoCID(deviceID=device)
        if not len(sn):
            self.socIDErrSignal.emit(FASTBOOT_ERROR_GET_SOCID)
            FastbootLampCommand.setRedOn(deviceID=device)
            return

        print(sn)

        mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'],port=int(self.sysXMLDict['mysqlport']),user=self.sysXMLDict['mysqluser'],\
                             passwd=self.sysXMLDict['mysqlpassword'],db=self.sysXMLDict['mysqldatabase'],table=self.sysXMLDict['mysqltable'])

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            FastbootLampCommand.setRedOn(deviceID=device)
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            return

        self.lock.acquire()
        snInDb = mysql.queryMysqlSNByMAC(mac=mac,stbType=self.sysXMLDict['mysqlstbtype'],poNumber=self.poNumber)
        if not snInDb:
            self.getSnErrSignal.emit(FASTBOOT_ERROR_GET_SERIALNUMBER)
            mysql.closeMysql()
            self.lock.release()
            FastbootLampCommand.setRedOn(deviceID=device)
            return
        elif sn != snInDb:
            self.printSNNotEqualInDBSignal.emit(PRINTER_SN_NOT_EQUAL_TO_DB)
            mysql.closeMysql()
            self.lock.release()
            FastbootLampCommand.setRedOn(deviceID=device)
            logging.error('sn local is not equal to sn in db.')
            return
        else:
            printFlag = MacSNPrint.sendInfoToPrinter(host=self.sysXMLDict['printerhost'],port=int(self.sysXMLDict['printerport']),sn=sn,mac=mac)
            if not printFlag:
                self.printMACSNErrSignal.emit(PRINTER_ERROR_MSG)
                FastbootLampCommand.setRedOn(deviceID=device)
            else:
                FastbootLampCommand.setGreenOn(deviceID=device)

        mysql.closeMysql()
        self.lock.release()

    def socIDFormatter(self,id):
        return ''.join(id.split('-'))

    def macFormatter(self,id):
        return ''.join(id.split(':'))

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
        # print(curDevices)
        # logging.info(curDevices)
        self.label_count.setText(str(len(curDevices)))

    def startCount(self):
        self.timerDevice.start(FASTBOOT_SHOW_DEVICES_COUNT_TIMEOUT)

    def showCurrentAvailableMAC(self):
        mysql = MySQLCommand(host=self.sysXMLDict['mysqlhost'],port=int(self.sysXMLDict['mysqlport']),user=self.sysXMLDict['mysqluser'],\
                             passwd=self.sysXMLDict['mysqlpassword'],db=self.sysXMLDict['mysqldatabase'],table=self.sysXMLDict['mysqltable'])

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            return

        self.lock.acquire()
        macCount = mysql.queryAvailableMACByStatus(self.poNumber,self.sysXMLDict['mysqlstbtype'])
        self.label_maccount.setText(str(macCount))
        self.lock.release()
        mysql.closeMysql()

    def onActionQueryTriggered(self):
        self.queryForm = QueryForm(self.sysXMLDict)
        self.queryForm.show()

    def showPONInputDialog(self):
        opN,okPressed = QInputDialog.getText(self,PO_INPUTDIALOG_TITLE,PO_INPUTDIALOG_PONUMBER_HINT,QLineEdit.Normal, " ")
        if okPressed and opN.strip():
            self.poNumber = opN
            self.lineedit_order.setText(self.poNumber)

        else:
            QMessageBox.critical(self,ERRORTITLE,PO_INPUTDIALOG_INFO)
            exit(1)

    def checkFastbootTool(self):
        if not os.path.exists('/usr/bin/fastboot') and not os.path.exists('fastboot'):
            QMessageBox.critical(self,ERRORTITLE,FASTBOOT_ERROR_NOT_INSTALLED)
            exit(1)

    def checkMysqldumpTool(self):
        if not os.path.exists('/usr/bin/mysqldump'):
            QMessageBox.critical(self,ERRORTITLE,MYSQL_ERROR_DUMP_NOT_INSTALLED)
            exit(1)


