#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 
@file: TestAllCase.py
@time:2018/8/20 16:38
"""
from testCase.testvote import *

def demo1():
    post_vote_excel()
    get_polls()

def demo2():
    get_demo()
    get_login()

if __name__ =='__main__':
    demo1()
    demo2()