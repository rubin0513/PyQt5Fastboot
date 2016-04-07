# -*- coding: utf-8 -*-
__author__ = 'djstava@gmail.com'

import xml.etree.ElementTree as ET
import logging

class XMLParser(object):
    def __init__(self,file):
        self.xmlFile = file
        self.burnTurpleFirst = []
        self.burnTurpleSecond = []

    def getTwoRoundTurple(self):
        tree = ET.parse(self.xmlFile)
        root = tree.getroot()

        for child in root.getchildren():
            if child.tag == 'FirstRound':
                for node in child:
                    dictBurn = {}
                    dictBurn['name'] = node.tag
                    dictBurn['address'] = node.attrib['address']
                    dictBurn['path'] = node.attrib['path']
                    dictBurn['md5'] = node.attrib['md5']
                    self.burnTurpleFirst.append(dictBurn)

            elif child.tag == 'SecondRound':
                for node in child:
                    dictBurn = {}
                    dictBurn['name'] = node.tag
                    dictBurn['address'] = node.attrib['address']
                    dictBurn['path'] = node.attrib['path']
                    dictBurn['md5'] = node.attrib['md5']
                    self.burnTurpleSecond.append(dictBurn)
            else:
                logging.error('No matched element.')

        return self.burnTurpleFirst,self.burnTurpleSecond

class SYSXMLParser(object):
    def __init__(self,file):
        self.xmlFile = file
        self.sysXMLDict = {}

    def getSysXMLDict(self):
        tree = ET.parse(self.xmlFile)
        root = tree.getroot()

        for child in root.getchildren():
            self.sysXMLDict[child.tag] = child.attrib
            self.sysXMLDict[child.tag] = child.text

            # if child.tag == 'FirstRound':
            #     for node in child:
            #         dictBurn = {}
            #         dictBurn['name'] = node.tag
            #         dictBurn['address'] = node.attrib['address']
            #         dictBurn['path'] = node.attrib['path']
            #         dictBurn['md5'] = node.attrib['md5']
            #         self.burnTurpleFirst.append(dictBurn)
            #
            # elif child.tag == 'SecondRound':
            #     for node in child:
            #         dictBurn = {}
            #         dictBurn['name'] = node.tag
            #         dictBurn['address'] = node.attrib['address']
            #         dictBurn['path'] = node.attrib['path']
            #         dictBurn['md5'] = node.attrib['md5']
            #         self.burnTurpleSecond.append(dictBurn)
            # else:
            #     logging.error('No matched element.')

        return self.sysXMLDict