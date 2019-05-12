#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.log

class TestLog(unittest.TestCase):
    def test_log(self):
        logger = moonhill.log.get_logger(__name__)
        logger.debug('this is a test')
        self.assertIsNotNone(logger)


if __name__ == '__main__':
    unittest.main()
