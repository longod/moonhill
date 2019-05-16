#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

# loggerすら隠蔽したいが、しばらくは互換性のある薄いwrap
# 1st stepは
# from logging import getLogger, DEBUG, Formatter, StreamHandler
# これをユーザが書かないようにすること
# なお、import loggingだけだと、うっかりlogging.deubg()も通ってしまう

CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

# use __name__
def getLogger(name):
    return logging.getLogger(name)

def StreamHandler(stream=None):
    return logging.StreamHandler(stream)

def FileHandler(filename, mode='a', encoding=None, delay=False):
    return logging.StreamHandler(filename, mode=mode, encoding=encoding, delay=delay)

def Formatter(fmt=None, datefmt=None, style='%'):
    return logging.Formatter(fmt=fmt, datefmt=datefmt, style=style)

class LoggerInitializer():
    instance = None

    def __init__(self):
        #print('initalize')
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.NullHandler()) # ユーザにハンドラを任せる
        logger.setLevel(logging.DEBUG)
        logger.propagate = True # 上位ロガーへの伝搬
        self.stdout_handler = StreamHandler(sys.stdout)
        self.formatter = Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] [%(funcName)s] %(message)s')
        self.stdout_handler.setFormatter(self.formatter)

if LoggerInitializer.instance is None:
    LoggerInitializer.instance = LoggerInitializer()


# get default setuped logger
# use __name__
def get_stdout_logger(name):
    logger = getLogger(name)
    logger.addHandler(LoggerInitializer.instance.stdout_handler)
    logger.setLevel(DEBUG)
    return logger

# def debug(msg, *args, **kwargs):
#     _logger = inlogger or __defaultlogger

