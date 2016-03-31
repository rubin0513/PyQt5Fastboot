# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

# log
LOGFILE = 'log.txt'

# how to use
HOWTOUSE = '软件使用方法'
HOWTOTEXT = "1、烧录过程共分2个阶段\r\n" \
            "2、点击相应按钮即可完成烧录\r\n" \
            "3、点击打印条码按钮完成条码打印"

# burn xml config file
CONFIGXML = 'config.xml'
XMLNOTFOUND = 'XML文件不存在'
IMAGEFILENOTFOUND = '镜像文件不存在'

# error message
ERRORTITLE = '出错了'
SUCCESSTITLE = '恭喜您'

# fastboot command
FASTBOOT_CMD_FLASH_PREFIX = 'fastboot flash -s '
FASTBOOT_CMD_DEVICES_PREFIX = 'fastboot devices -l'
FASTBOOT_CMD_SOCID_PREFIX = 'fastboot getvar socid -s '
FASTBOOT_CMD_CALCCPCB_PREFIX = 'fastboot getvar calccpcb -s '

FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE = '没有设备上线'
FASTBOOT_ERROR_GET_SOCID = '获取设备号失败'
FASTBOOT_ERROR_CALC_CPCB = '计算CPCB出错'
FASTBOOT_ERROR_GET_MAC = '获取MAC地址出错'
FASTBOOT_ERROR_UPDATE_SN = '更新序列号出错,序列号已存在'
FASTBOOT_ERROR_SECONDROUND_NEEDED = '第一阶段烧录已完成，请进行第二阶段烧录!'
FASTBOOT_ERROR_FIRSTROUND_NEEDED = '请先进行第一阶段烧录!'
FASTBOOT_ERROR_TIMEOUT_IN_SECONDS = 3

BURN_ERROR_KEYWORD = 'FAILED'
FASTBOOT_DEVICES_KEYWORD = 'fastboot'
FASTBOOT_SOCID_KEYWORD = 'socid:'
FASTBOOT_CPCB_KEYWORD = 'sucess'

BURN_ERROR = '烧录失败'
BURN_FIRST_ROUND_OK = '第一阶段烧录成功!'
BURN_SECOND_ROUND_OK = '第二阶段烧录成功!'

# checksum
CHECKSUM_ERROR = '镜像校验出错'
CHECKSUM_COUNT = 1048576

# mysql settings
MYSQL_HOST = '10.10.10.240'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'longjingdb'
MYSQL_TABLE = 'mac'
STBTYPE = 'L6000-I'
MYSQL_CONNECT_ERROR = '数据库无法连接'

# Irdeto Key
IRDETO_IRDETO_LIB_PATH = 'IrdKey/liblj_key.so'
IRDETO_CRC_LIB_PATH = 'IrdKey/libcrc.so'
IRDETO_KEY_SIZE = 512
IRDETO_CADATA_FILE = 'cadata.img'
IRDETO_GET_KEY_ERROR = '获取Irdeto Key出错'
IRDETO_CUSTOM_KEY = 0
IRDETO_DEVELOP_KEY = 1