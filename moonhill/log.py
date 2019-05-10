#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

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

# and more helpers
