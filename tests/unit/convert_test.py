#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.convert

class TestConvert(unittest.TestCase):
    def test_safe_cast(self):
        self.assertEqual( moonhill.convert.safe_cast(1, str, '0'), '1')
        self.assertEqual( moonhill.convert.safe_cast('1', int, 0), 1)
        self.assertEqual( moonhill.convert.safe_cast('a', int, 0), 0)

if __name__ == '__main__':
    unittest.main()
