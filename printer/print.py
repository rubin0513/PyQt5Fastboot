# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import socket
import logging

from common.constant import PRINTER_OP_TIMEOUT

class MacSNPrint(object):
    def __init__(self):
        pass

    @classmethod
    def sendInfoToPrinter(self,host,port,sn,mac):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(PRINTER_OP_TIMEOUT)
        flag = False

        try:
            sock.connect((host, port))
        except:
            print('connect printer failed.')
            logging.error('connect printer failed.')
            flag = False
            sock.close()
            return flag

        while True:
            buffStart = sock.recv(PRINTER_DEFAULT_SIZE)
            print(buffStart)

            if buffStart == PRINTER_SERVER_START:
                if len(sn) != 11:
                    sn = '901' + sn
                buff = sn + ' ' + mac + '|'
                print('send printer:' + buff)
                logging.info('send printer:' + buff)
                sock.send(buff.encode('utf-8'))
                break
            else:
                print("no send buff.")

        while True:
            buffOver = sock.recv(PRINTER_DEFAULT_SIZE)
            print(buffOver)

            if buffOver == PRINTER_SERVER_OVER:
                print("succ")
                flag = True
                break
            else:
                print("no recv ok.")

        sock.close()
        return flag