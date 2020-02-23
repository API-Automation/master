#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:hanyanlin time:2020/2/21
import logging
import time
import logging.handlers
from master.config.config import LOG_DIR

class Logger(object):
    """
        This is the class to wrap logging module
    """

    def __init__(self, logger, file_level=logging.DEBUG):
        #logging类实例化
        self.logger = logging.getLogger(logger)
        #设置日志默认级别
        self.logger.setLevel(logging.DEBUG)
        #设置日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        #设置日志文件名称
        self.LogFileName = LOG_DIR + r'/' + 'log_' + time.strftime("%Y-%m-%d") +'.log'
        # 设置日志文件大小达到100M后进行切割log file
        lf =logging.handlers.RotatingFileHandler(self.LogFileName, maxBytes=100*1024*1024,backupCount=5,encoding=None, delay=False)
        lf.setFormatter(formatter)
        # 设置日志级别
        lf.setLevel(file_level)
        # 设置控制台输出Console output
        co = logging.StreamHandler()
        co.setFormatter(formatter)
        co.setLevel(file_level)
        # handle有效
        self.logger.addHandler(lf)
        self.logger.addHandler(co)

    def debugInfo(self, message):
        self.logger.debug(message)

    def info_log(self, message):
        self.logger.info(message)

    def warning_log(self, message):
        self.logger.warning(message)

    def error_log(self, message):
        self.logger.error(message)



if __name__ == '__main__':
    for i in range(0, 100):
        log = Logger("实例化", file_level=logging.DEBUG)
        log.debugInfo('debugInfo')
        log.info_log('info_log')
        log.error_log("error_log")
        log.warning_log("warning_log")
        log.logger.log(logging.ERROR, '%(module)s %(info)s', {'module': 'log日志', 'info': 'error'})
        time.sleep(1)
