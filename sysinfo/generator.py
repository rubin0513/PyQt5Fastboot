# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import json
import subprocess
import hashlib
import os
import glob
import logging
import shutil

def RemoveFilesByExtName(dir = '.', ext = '*.o'):
    for i in glob.glob(os.path.join(dir, ext)):
        os.remove(i)

def DoCompile(args, **kwargs):
    return subprocess.Popen(args, **kwargs)

def NeedToGenerateLib(gcc_path):
    if (not (os.path.exists("../sysinfo_lib/sysinfo.c") \
        and os.path.exists("../sysinfo_lib/utility.c") \
        and os.path.exists(gcc_path))):
        return False
    return True

def generate_sysinfolib(compiler, ld_path):
    # print "compiler = %s\n" % (compiler)
    cmd = [compiler + 'gcc', "-fPIC", "-shared"]
    cmd.extend(["-o", "libsysinfo.so",
        "../sysinfo_lib/sysinfo.c", "../sysinfo_lib/utility.c", "-L"+ \
        ld_path + "../arm-none-linux-gnueabi/libc/usr/lib", "-lc"])
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate libsysinfo.so failed!"
    cmd = [compiler + 'gcc', "-c", "../sysinfo_lib/utility.c", "-o", "utility.o"]
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate utility.o failed!"
    cmd = [compiler + 'gcc', "-c", "../sysinfo_lib/sysinfo.c", "-o", "sysinfo.o"]
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate sysinfo.o failed!"
    cmd = [compiler + 'ar', 'crv']
    cmd.extend(["libsysinfo.a", "sysinfo.o", "utility.o"])
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate libsysinfo.a failed!"
    RemoveFilesByExtName('.', '*.o')
    cmd = [compiler + 'gcc', "-D__UBOOT_SYSINFO__"]
    cmd.extend(['-o', 'utility.o', '-c', '../sysinfo_lib/utility.c'])
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate utility.o failed!"
    cmd = [compiler + 'gcc', "-D__UBOOT_SYSINFO__"]
    cmd.extend(['-o', 'sysinfo.o', '-c', '../sysinfo_lib/sysinfo.c'])
    p = DoCompile(cmd, stdout=subprocess.PIPE)
    p.communicate()
    assert p.returncode == 0, "generate sysinfo.o failed!"

def calcMd5(str):
    md5 = hashlib.md5()
    md5.update(str.encode("utf-8"))
    return md5.hexdigest()

def length(str):
    return len(str.encode('utf-8'))

def parse_partition_size(str):
    str = str.upper()
    ty = str[-1]
    sz = str[:-1]
    size_table = {
        'B' : 1,
        'K': 1024,
        'M': 1024 * 1024,
        'G': 1024*1024*1024
    }

    return int(sz) * size_table[ty]

def write_sysinfo(dictionary,modifyDict):
    dirPrex = "soc" + modifyDict['STB_ID']
    if not os.path.exists(dirPrex):
        os.mkdir(dirPrex)
    else:
        if os.path.exists(dirPrex + "/systeminfo_rw.img"):
            os.remove(dirPrex + "/systeminfo_rw.img")

        if os.path.exists(dirPrex + "/systeminfo_ro.img"):
            os.remove(dirPrex + "/systeminfo_ro.img")

    wf = open(dirPrex + "/systeminfo_rw.img", "wb")
    rf = open(dirPrex + "/systeminfo_ro.img", "wb")
    ver = dictionary['version']
    vendor = dictionary['vendor']
    gcc_path = dictionary['toolchain_path'] + '/'+ dictionary['toolchain_prefix']
    if NeedToGenerateLib(dictionary['toolchain_path']):
        generate_sysinfolib(gcc_path, dictionary['toolchain_path'] + "")

    arr = {'sysinfo_rw' : wf, 'sysinfo_ro' : rf}

    magicnumber = {'sysinfo_rw' : 'SYSTEMINFORW',
                   'sysinfo_ro' : 'SYSTEMINFORO'}

    length_table = {'magic' : 100, 'permission' : 2,
                    'size' : 20, 'offset' : 10,
                    'ver' : 10, 'vendor' : 512,
                    'crc' : 256, 'key' : 32,
                    'value' : 512,  'time' : 8,
                    'blockcount' : 2, 'md5' : 32};

    firstBlockPos = length_table['magic'] + length_table['vendor'] + length_table['ver'] \
        + length_table['size'] + length_table['blockcount'] + length_table['offset'] \
        + length_table['md5']

    for partition in arr:
        partSize = parse_partition_size(dictionary[partition]['size'])
        arr[partition].write('\x00'.encode("utf-8") * partSize)
        arr[partition].seek(0, 0)
        header_md5_str = magicnumber[partition] + ('\x00' * (length_table['magic'] - length(magicnumber[partition])))
        header_md5_str += vendor + ('\x00' * (length_table['vendor'] - length(vendor)))
        header_md5_str += ver + ('\x00' * (length_table['ver'] - length(ver)))
        part_size = '%d' % (partSize)
        header_md5_str += part_size + ('\x00' * (length_table['size'] - length(part_size)))
        count = len(dictionary[partition]['blocks'])
        countStr = '%d' % (count)
        header_md5_str += countStr + ('\x00' * (length_table['blockcount'] - length(countStr)))

        firstBlockOffset = dictionary[partition]['blocks'][0]['offset']
        header_md5_str += firstBlockOffset + ('\x00' * (length_table['offset'] - length(firstBlockOffset)))
        '''partition header md5 calc'''
        md5 = calcMd5(header_md5_str)
        header_md5_str += md5
        arr[partition].write(header_md5_str.encode("utf-8"))
        arr[partition].seek(int(partSize / 2), 0)
        arr[partition].write(header_md5_str.encode("utf-8"))

        for index in range(count):
            offset = dictionary[partition]['blocks'][index]['offset']
            arr[partition].seek(int(offset, 16), 0)
            block_md5_str = offset + ('\x00' * (length_table['offset'] - length(offset)))
            if index == len(dictionary[partition]['blocks']) - 1:
                nextoffset = '0x0'
            else:
                nextoffset = dictionary[partition]['blocks'][index + 1]['offset']
            block_md5_str += nextoffset + ('\x00' * (length_table['offset'] - length(nextoffset)))
            arr[partition].write(block_md5_str.encode("utf-8"))
            arr[partition].seek(int(partSize / 2) + int(offset, 16), 0)
            arr[partition].write(block_md5_str.encode("utf-8"))

            arr[partition].seek(int(offset, 16) + length(block_md5_str), 0)
            md5Pos = arr[partition].tell()
            arr[partition].seek(length_table['md5'], 1)
            md5str = ''
            for key_value in dictionary[partition]['blocks'][index]['sysinfo']:
                if key_value['key'] in modifyDict.keys():
                    key_value['value'] = modifyDict[key_value['key']]

                md5str += key_value['key'] + ('\x00' * (length_table['key'] - length(key_value['key'])))
                md5str += key_value['value'] + ('\x00' * (length_table['value'] - length(key_value['value'])))
                md5str += '00000000'

            arr[partition].write(md5str.encode("utf-8"))
            arr[partition].seek(int(partSize / 2) + md5Pos + length_table['md5'], 0)
            arr[partition].write(md5str.encode("utf-8"))
            md5 = calcMd5(block_md5_str + md5str)
            arr[partition].seek(md5Pos, 0)
            arr[partition].write(md5.encode("utf-8"))
            arr[partition].seek(int(partSize / 2) + md5Pos, 0)
            arr[partition].write(md5.encode("utf-8"))

    wf.close()
    rf.close()

def process_json(jsonFile,dict):
    print(dict)
    logging.info(dict)
    jsonfile = open(jsonFile, "rb")
    data = jsonfile.read()
    json_dict = json.loads(data.decode("utf-8"))
    write_sysinfo(json_dict,dict)
    jsonfile.close()
