# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

from PyQt5.QtWidgets import QMessageBox,QWidget

from ui.ui_query import *
from db.mysql import *
from common.constant import QUERY_FORM_TITLE,ERRORTITLE,QUERY_PON_IS_EMPTY

class QueryForm(QWidget, Ui_Form):
    def __init__(self,mysqlDict,parent=None):

        super(QueryForm,self).__init__(parent)
        self.setupUi(self)

        self.host = mysqlDict['mysqlhost']
        self.port = mysqlDict['mysqlport']
        self.user = mysqlDict['mysqluser']
        self.passwd = mysqlDict['mysqlpassword']
        self.database = mysqlDict['mysqldatabase']
        self.table = mysqlDict['mysqltable']

        self.button_po.clicked.connect(self.onButtonPOClicked)

    def onButtonPOClicked(self):
        poNum = self.lineEdit_po.text()
        print(poNum)

        if(len(poNum) == 0):
            QMessageBox.information(self.button_po,ERRORTITLE,QUERY_PON_IS_EMPTY)
            return

        mysql = MySQLCommand(host=self.host,port=int(self.port),user=self.user,\
                             passwd=self.passwd,db=self.database,table=self.table)

        mysqlConFlag = mysql.connectMysql()
        if not mysqlConFlag:
            self.mysqlConnectErrSignal.emit(MYSQL_CONNECT_ERROR)
            return

        macCount = mysql.queryAvailableMACByPON(pon=poNum)
        mysql.closeMysql()
        msg = "订单号" + poNum + "的可用MAC数是: " + str(macCount)
        QMessageBox.information(self.button_po,QUERY_FORM_TITLE,msg)