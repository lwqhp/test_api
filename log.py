#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 生成日志类
@file: log.py
@time:2018/9/2 12:45
"""

import logging
from logging.handlers import RotatingFileHandler
import threading
from testdata.getpath import GetTestLogPath, GetTestConfig
import configparser

class LogSignleton(object):
    def __init__(self):
        pass

    def __new__(cls):
        config = configparser.ConfigParser()
        config.read(GetTestConfig("logconfig.conf"),encoding='utf-8-sig')
        loging = 'LOGGER'
        mutex = threading.Lock()
        mutex.acquire() #上锁，防止多线程下出问题
        if not hasattr(cls,'instance'):
            cls.instance = super(LogSignleton,cls).__new__(cls)
            cls.instance.log_filename = GetTestLogPath()
            cls.instance.max_bytes_each = config[loging]['max_bytes_each']
            cls.instance.backup_count = config[loging]['backup_count']
            cls.instance.fmt = config[loging]['fmt']
            cls.instance.log_level_in_console = config[loging]['log_level_in_console']
            cls.instance.log_level_in_logfile = config[loging]['log_level_in_logfile']
            cls.instance.logger_name = "test_logger"
            cls.instance.console_log_on = config[loging]['console_log_on']
            cls.instance.logfile_log_on = config[loging]['logfile_log_on']
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return self.logger

    def __config_logger(self):
        #设置日志格式
        fmt = self.fmt.replace('|','%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1:
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1 :
            rt_file_handler = RotatingFileHandler(self.log_filename,maxBytes=self.max_bytes_each,backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)

logsingleton = LogSignleton()
logger = logsingleton.get_logger()

if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')

    #使用
    #from log import logger
    #logger.info('')
