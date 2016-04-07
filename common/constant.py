# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

# log
LOGFILE = 'log.txt'

# how to use
HOWTOUSE = '软件使用方法'
HOWTOTEXT = "1、烧录过程共分2个阶段\r\n" \
            "2、点击相应按钮即可完成烧录\r\n" \
            "3、点击打印条码按钮完成条码打印\r\n" \

# burn xml config file
CONFIGXML = 'lj/config.xml'
CONFIGSYSXML = 'lj/sys.xml'
XMLNOTFOUND = '镜像配置文件不存在'
SYSXMLNOTFOUND = '系统配置文件不存在'
IMAGEFILENOTFOUND = '镜像文件不存在'
SYSINFOJSONFILE = 'lj/sysinfo.json'

# error message
ERRORTITLE = '出错了'
SUCCESSTITLE = '恭喜您'

# fastboot command
FASTBOOT_CMD_FLASH_PREFIX = 'fastboot flash -s '
FASTBOOT_CMD_DEVICES_PREFIX = 'fastboot devices -l'
FASTBOOT_CMD_SOCID_PREFIX = 'fastboot getvar socid -s '
FASTBOOT_CMD_CALCCPCB_PREFIX = 'fastboot getvar calccpcb -s '
FASTBOOT_CMD_MAC_PREFIX = 'fastboot getvar getmac -s '
FASTBOOT_CMD_LAMP_RED_ON = 'fastboot getvar redon -s '
FASTBOOT_CMD_LAMP_RED_FAST = 'fastboot getvar redfast -s '
FASTBOOT_CMD_LAMP_RED_SLOW = 'fastboot getvar redslow -s '
FASTBOOT_CMD_LAMP_GREEN_ON = 'fastboot getvar greenon -s '
FASTBOOT_CMD_LAMP_GREEN_FAST = 'fastboot getvar greenfast -s '
FASTBOOT_CMD_LAMP_GREEN_SLOW = 'fastboot getvar greenslow -s '

FASTBOOT_ERROR_MSG_NO_DEVICE_ONLINE = '没有设备上线'
FASTBOOT_ERROR_GET_SOCID = '获取设备号失败'
FASTBOOT_ERROR_CALC_CPCB = '计算CPCB出错'
FASTBOOT_ERROR_GET_MAC = '获取MAC地址出错'
FASTBOOT_ERROR_UPDATE_SN = '更新序列号出错'
FASTBOOT_ERROR_SECONDROUND_NEEDED = '第一阶段烧录已完成，请进行第二阶段烧录!'
FASTBOOT_ERROR_FIRSTROUND_NEEDED = '请先进行第一阶段烧录!'
FASTBOOT_ERROR_TIMEOUT_IN_SECONDS = 3
FASTBOOT_ERROR_GET_SERIALNUMBER = '获取序列号出错'
FASTBOOT_SHOW_DEVICES_COUNT_TIMEOUT = 3000

BURN_ERROR_KEYWORD = 'FAILED'
FASTBOOT_DEVICES_KEYWORD = 'fastboot'
FASTBOOT_SOCID_KEYWORD = 'socid:'
FASTBOOT_CPCB_KEYWORD = 'sucess'
FASTBOOT_LAMP_OK_KEYWORD = 'OK'
FASTBOOT_GETMAC_KEYWORD = 'getmac:'

BURN_ERROR = '烧录失败'
BURN_FIRST_ROUND_OK = '第一阶段烧录完成!'
BURN_SECOND_ROUND_OK = '第二阶段烧录成功!'

# checksum
CHECKSUM_ERROR = '镜像校验出错'
CHECKSUM_COUNT = 1048576

# mysql settings
# MYSQL_HOST_DEFAULT = '192.168.1.50'
# MYSQL_PORT_DEFAULT = 3306
# MYSQL_USERNAME_DEFAULT = 'root'
# MYSQL_PASSWORD_DEFAULT = 'toor'
# MYSQL_DATABASE_DEFAULT = 'longjingdb'
# MYSQL_TABLE_DEFAULT = 'mac'
# STBTYPE_DEFAULT = 'L6000'
MYSQL_CONNECT_ERROR = '数据库无法连接'

# Irdeto Key
IRDETO_IRDETO_LIB_PATH = 'lj/liblj_key.so'
IRDETO_CRC_LIB_PATH = 'lj/libcrc.so'
IRDETO_KEY_SIZE = 512
IRDETO_CADATA_FILE = 'cadata.img'
IRDETO_GET_KEY_ERROR = '获取Irdeto Key出错'
IRDETO_CUSTOM_KEY = 0
IRDETO_DEVELOP_KEY = 1

# Printer
# PRINTER_SERVER_DEFAULT = '192.168.1.51'
# PRINTER_PORT_DEFAULT = 4001
PRINTER_DEFAULT_SIZE = 16
PRINTER_SERVER_START = b'Hello'
PRINTER_SERVER_OVER = b'ok'
PRINTER_OK_MSG = '条码打印成功'
PRINTER_BURN_NEEDED_MSG = '请先进行软件烧录'
PRINTER_OP_TIMEOUT = 5
PRINTER_ERROR_MSG = '条码打印失败'