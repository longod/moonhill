#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.log

class TestLog(unittest.TestCase):
    def test_log(self):
        logger = moonhill.log.getDefaultLogger(__name__)
        # handler = moonhill.log.StreamHandler(sys.stdout)
        # formatter = moonhill.log.Formatter('%(asctime)s %(levelname)s %(name)s %(funcName)s: %(message)s')
        # handler.setFormatter(formatter)
        # logger.addHandler(handler)
        # logger.setLevel(moonhill.log.DEBUG)
        logger.debug('this is a test')
        self.assertIsNotNone(logger)


if __name__ == '__main__':
    unittest.main()
