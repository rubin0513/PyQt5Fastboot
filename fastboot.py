# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import sys
import subprocess
import random
import common

def lj_list_device_id(self):
        '''
        扫描当前连接的设备
        :return: 返回连接设备的设备号
        '''

        process = subprocess.Popen(common.FLASH_DEVICE,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        device_id = process.stdout.read().rstrip(b'\tfastboot\r\n')
        process.stdout.close()
        print(device_id.decode("utf-8"))
        return device_id.decode("utf-8")

def lj_get_default_image_path(imageName):
    '''

    :param imageName:输入文件名
    :return:返回输入文件名的绝对路径
    '''

    return os.path.abspath(imageName)

def lj_generate_random_number():
    '''
    产生一个随机数
    :return:返回产生的随机数
    '''

    return random.randint(0,sys.maxsize)