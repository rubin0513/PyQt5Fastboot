# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

PREVIOUS_DATA = '001122334455'
FLAG_DEVICE_ONLINE = False
HOWTOTEXT = "1、当Android设备以fastboot模式上线时，顶部的文本框中会显示当前连接设备的ID号\r\n" \
            "2、选择相应的镜像文件,默认情况下会自动选择当前toc目录下的对应文件\r\n" \
            "3、单独烧录请点击对应镜像后面的烧录按钮\r\n" \
            "4、全部烧录按钮会根据当前选中的镜像文件依次进行烧录\r\n" \
            "5、烧录完毕后可以选择重启设备或继续启动\r\n" \
            "6、如有任何问题或建议，请联系djstava@gmail.com\r\n"

BBCB_OFFSET = 0x200000
BBCB_STRUCT_SIZE = 24

SECBOOT_ADDRESS = "1o0"
SECOS_ADDRESS = "2o0"
SECOS_BACK_ADDRESS = "2o800"
UBOOT_ADDRESS = "1o80"
UBOOT_BACK_ADDRESS = "1o880"

UBOOT_ENV_ADDRESS = "Oo22"
DEVICETREE_ADDRESS = "Oo2022"
DEVICEINFO_ADDRESS = "Oo2800"
MISC_ADDRESS = "Oo2c00"
SPLASH_ADDRESS = "Oo3000"
NVRAM_ADDRESS = "Oo7000"
LJINFO_ADDRESS = "Oob000"
KERNELOTA_ADDRESS = "Oo13000"
MINIDVB_ADDRESS = "Oo23000"
CALIB_ADDRESS = "Oo43000"
DVBDATA_ADDRESS = "Oo4b000"
BOOT_ADDRESS = "Oo5b000"
RECOVERY_ADDRESS = "Oo6b000"
SYSTEM_ADDRESS = "Oo7b000"
CACHE_ADDRESS = "Oo27b000"
USERDATA_ADDRESS = "Oo37b000"

BURN_ERROR_KEYWORD = "FAILED"
FLASH_PREFIX = "fastboot.exe flash "
PMP_ADDRESS = " pmp "

FLASH_REBOOT = "fastboot.exe reboot"
FLASH_CONTINUE = "fastboot.exe continue"

LOGFILE = "PyQt5Fastboot.log"
BURNSUCCESS = "恭喜您"
BURNERROR = "很抱歉"
HOWTOUSE = "软件使用方法"