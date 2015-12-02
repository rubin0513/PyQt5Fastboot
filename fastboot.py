# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import os
import sys
import subprocess
import random

def lj_list_device_id(self):
        '''
        扫描当前连接的设备
        :return: 返回连接设备的设备号
        '''

        process = subprocess.Popen('fastboot.exe devices',shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        str = process.stdout.read().rstrip(b'\tfastboot\r\n')

        return str.decode("utf-8")

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

def lj_generate_bcd_code(str):
    '''
    生成字符串对应的BCD码
    :return:返回产生BCD码字符串
    '''

    return ''.join(chr(int(str[i:i+2], 16)) for i in range(0, len(str), 2))