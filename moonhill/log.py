#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

class LoggerInitializer():
    initializer = None
    def __init__(self):
        #print('initalize')
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.NullHandler()) # ユーザにハンドラを任せる
        logger.setLevel(logging.DEBUG)
        logger.propagate = True # 上位ロガーへの伝搬

if LoggerInitializer.initializer is None:
    LoggerInitializer.initializer = LoggerInitializer()

# loggerすら隠蔽したいが、しばらくは互換性のある薄いwrap
# 1st stepは
# from logging import getLogger, DEBUG, Formatter, StreamHandler
# これをユーザが書かないようにすること
# なお、import loggingだけだと、うっかりlogging.deubg()も通ってしまう

DEBUG = logging.DEBUG
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

# use __name__
def getDefaultLogger(name):
    logger = getLogger(__name__)
    handler = StreamHandler(sys.stdout)
    formatter = Formatter('%(asctime)s %(levelname)s %(name)s %(funcName)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    return logger

# def debug(msg, *args, **kwargs):
#     _logger = inlogger or __defaultlogger

