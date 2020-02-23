#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:hanyanlin time:2020/2/22
import os
# 项目目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置文件路径
CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
#测试用例路径
CASE_DIR=os.path.join(ROOT_DIR,'testCases')
#测试数据路径
DATA_DIR = os.path.join(ROOT_DIR, 'testData')
# 日志文件存放路径
LOG_DIR = os.path.join(ROOT_DIR, 'log')
#报告路径
REPORT_DIR=os.path.join(ROOT_DIR,'report')