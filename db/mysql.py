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
            if self.cursor.execute(sql):
                row = self.cursor.fetchone()
                if row:
                    updateSql = "UPDATE " + self.table + " SET status='1' WHERE macAddr0='" + row[1] + "' and stbType='" + stbType + "' and po='" + poNumber + "'"
                    print("update status:" + updateSql)
                    logging.info("update status:" + updateSql)

                    if self.cursor.execute(updateSql):
                        self.conn.commit()
                        return row[1]
                    else:
                        self.conn.rollback()
                        print(updateSql + " failed.")
                        logging.error(updateSql + " failed.")
            else:
                print(sql + ' execute failed.')
                logging.error(sql + ' execute failed.')
        except:
            logging.error('query error.')

    def updateMysqlSN(self,mac,sn,stbType,poNumber):
        sql = "UPDATE " + self.table + " SET sn='" + sn + "'" + " WHERE macAddr0='" + mac + "' and stbType='" + stbType + "' and po='" + poNumber + "'"
        print("update sn:" + sql)
        logging.info("update sn:" + sql)

        try:
            if self.cursor.execute(sql):
                self.conn.commit()
                self.flag = True
            else:
                self.conn.rollback()
                self.flag = False

            return self.flag
        except:
            logging.error('update sn error.')

    def resetMysqlMACStatus(self,mac,stbType,poNumber):
        sql = "UPDATE " + self.table + " SET status='0' WHERE macAddr0='" + mac + "' and stbType='" + stbType + "' and po='" + poNumber + "'"
        print("update MAC status:" + sql)
        logging.info("update MAC status:" + sql)

        try:
            if self.cursor.execute(sql):
                self.conn.commit()
                self.flag = True
            else:
                self.conn.rollback()
                self.flag = False

            return self.flag
        except:
            logging.error('reset mac status error.')

    def resetMysqlMACStatusAndSN(self,mac,stbType,poNumber):
        sql = "UPDATE " + self.table + " SET status='0',sn=NULL WHERE macAddr0='" + mac + "' and stbType='" + stbType + "' and po='" + poNumber + "'"
        print("reset MAC status:" + sql)
        logging.info("reset MAC status:" + sql)

        try:
            if self.cursor.execute(sql):
                self.conn.commit()
                self.flag = True
            else:
                self.conn.rollback()
                self.flag = False

            return self.flag
        except:
            logging.error('reset mac & sn error.')

    def queryMysqlSNByMAC(self,mac,stbType,poNumber):
        sql = "SELECT * FROM " + self.table + " WHERE macAddr0='" + mac + "' and stbType='" + stbType + "' and po='" + poNumber + "' and status='1'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)

        try:
            if self.cursor.execute(sql):
                row = self.cursor.fetchone()
                if row:
                    return row[3]
            else:
                print(sql + ' execute failed.')
                logging.error(sql + ' execute failed.')
        except:
            logging.error('query mac & sn error.')

    def queryMysqlSN(self,sn,mac,stbType,poNumber):
        sql = "SELECT * FROM " + self.table + " WHERE sn='" + sn + "' and macAddr0='" + mac + "' and stbType='" + stbType + "' and po='" + poNumber + "' and status='1'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)
        flag = False

        try:
            if self.cursor.execute(sql):
                row = self.cursor.fetchone()
                if row:
                    flag = True
            else:
                print(sql + ' execute failed.')
                logging.error(sql + ' execute failed.')
                flag = False

            return flag
        except:
            logging.error('query sn error.')

    def queryAvailableMACByStatus(self,poNumber,stbType):
        sql = "SELECT count(*) FROM " + self.table + " WHERE status='0' and po='" + poNumber + "' and stbType='" + stbType + "'"
        # print("query sql: " + sql)
        # logging.info("query sql: " + sql)

        try:
            if self.cursor.execute(sql):
                row = self.cursor.fetchall()
                # print(row[0][0])

            else:
                print(sql + ' execute failed.')
                logging.error(sql + ' execute failed.')

            return row[0][0]
        except:
            print('query available mac error.')
            logging.error('query available mac error.')

    # Not used
    def queryAvailableMACByPON(self,pon):
        sql = "SELECT count(*) FROM " + self.table + " WHERE po='" + pon +"' and status='0'"
        print("query sql: " + sql)
        logging.info("query sql: " + sql)

        try:
            if self.cursor.execute(sql):
                row = self.cursor.fetchall()
                print(row[0][0])

            else:
                print(sql + ' execute failed.')
                logging.error(sql + ' execute failed.')

            return row[0][0]
        except:
            logging.error('query avaiable mac by pon error.')

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()