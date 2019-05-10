#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.log
from logging import getLogger, DEBUG, Formatter, StreamHandler

class TestLog(unittest.TestCase):
    def test_log(self):
        logger = getLogger(__name__)
        handler = StreamHandler(sys.stdout)
        formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(DEBUG)
        logger.debug('this is a test')
        self.assertIsNotNone(logger)


if __name__ == '__main__':
    unittest.main()
