#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
# from .. import moonhill.log # これがかけない…
# from .. import moonhill これはいけるのに…
# from ..moonhill import log これはいけるのに…
sys.path.append(os.getcwd())
import moonhill.log

class TestLog(unittest.TestCase):
    def test_log(self):
        logger = moonhill.log.get_stdout_logger(__name__)
        self.assertIsNotNone(logger)
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')


if __name__ == '__main__':
    unittest.main()
