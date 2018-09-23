#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 
@file: getpath.py
@time:2018/8/12 21:55
"""
import os
import time

def GetTestDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"testdata","TestData.xls")

#生在测试报表的路径
def GetTestReport():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "testreport", now +"TestReport.xls")

#日志路径
def GetTestLogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "logs", "log.txt")

#配置文件路径
def GetTestConfig(configname):
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", configname)

#print(GetTestDataPath())