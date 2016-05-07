# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import logging
import pymysql

class MySQLCommand(object):
    def __init__(self,host,port,user,passwd,db,table):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.table = table
        self.flag = False

    def connectMysql(self):
        flag = True

        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db,connect_timeout=3,charset='utf8')
            self.cursor = self.conn.cursor()
            flag = True
        except:
            print('connect mysql error.')
            logging.error('connect mysql error.')
            flag = False

        return flag

    def queryMysql(self,stbType,poNumber):
        sql = "SELECT * FROM " + self.table + " WHERE status='0' and stbType='" + stbType + "' and po='" + poNumber + "'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            if row:
                updateSql = "UPDATE " + self.table + " SET status='1' WHERE macAddr0='" + row[1] + "'"
                print("update status:" + updateSql)
                logging.info("update status:" + updateSql)
                try:
                    self.cursor.execute(updateSql)
                    self.conn.commit()
                    return row[1]
                except:
                    self.conn.rollback()
                    print(updateSql + " failed.")
                    logging.error(updateSql + " failed.")
        except:
            print(sql + ' execute failed.')
            logging.error(sql + ' execute failed.')

    def updateMysqlSN(self,mac,sn):
        sql = "UPDATE " + self.table + " SET sn='" + sn + "'" + " WHERE macAddr0='" + mac + "'"
        print("update sn:" + sql)
        logging.info("update sn:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.flag = True
        except:
            self.conn.rollback()
            self.flag = False

        return self.flag

    def resetMysqlMACStatus(self,mac):
        sql = "UPDATE " + self.table + " SET status='0' WHERE macAddr0='" + mac + "'"
        print("update MAC status:" + sql)
        logging.info("update MAC status:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            self.flag = True
        except:
            self.conn.rollback()
            self.flag = False

        return self.flag

    def queryMysqlSNByMAC(self,mac):
        sql = "SELECT * FROM " + self.table + " WHERE macAddr0='" + mac + "'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            if row:
                return row[3]
        except:
            print(sql + ' execute failed.')
            logging.error(sql + ' execute failed.')

    def queryMysqlSN(self,sn):
        sql = "SELECT * FROM " + self.table + " WHERE sn='" + sn + "'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)
        flag = False

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            if row:
                flag = True
        except:
            print(sql + ' execute failed.')
            logging.error(sql + ' execute failed.')

        return flag

    def queryAvailableMACByStatus(self,poNumber):
        sql = "SELECT count(*) FROM " + self.table + " WHERE status='0' and po='" + poNumber + "'";
        print("query sql: " + sql)
        # logging.info("query sql: " + sql)

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(row[0][0])

        except:
            print(sql + ' execute failed.')
            logging.error(sql + ' execute failed.')

        return row[0][0]

    def queryAvailableMACByPON(self,pon):
        sql = "SELECT count(*) FROM " + self.table + " WHERE po='" + pon +"' and status='0'";
        print("query sql: " + sql)
        logging.info("query sql: " + sql)

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchall()
            print(row[0][0])

        except:
            print(sql + ' execute failed.')
            logging.error(sql + ' execute failed.')

        return row[0][0]

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()