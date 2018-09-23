#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 
@file: TestAllRunner.py
@time:2018/8/20 16:40
"""
import threading
from TestAllCase import *

def threads():
    threads=[]
    threads.append(threading.Thread(target=demo1))
    threads.append(threading.Thread(target=demo2))
    for th in threads:
        th.start()
    [th.join() for th in threads]

if __name__ =='__main__':
    threads()