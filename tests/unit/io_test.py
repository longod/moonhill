#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.io

class TestIO(unittest.TestCase):
    def test_text(self):
        path = 'temp/test.txt'
        moonhill.io.write_text(path, path)
        r = moonhill.io.read_text(path)
        self.assertEqual(path, r)


if __name__ == '__main__':
    unittest.main()
