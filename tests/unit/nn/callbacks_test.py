#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.nn
import keras

# callbacks は integration testでやらないと意味が薄い, kerasもunit testは無い

class TestCallbacks(unittest.TestCase):
    def test_persistent(self):
        c = moonhill.nn.callbacks.PersistentHistory()
        # initialize of super's constructor
        self.assertIsNone(c.model)
        self.assertIsNone(c.validation_data)
        self.assertEqual( c.initial_epoch(), 0)
        self.assertEqual( c.last_initial_epoch, 0)
        self.assertEqual( c.epochs(1), 1)
        self.assertEqual( c.last_initial_epoch, 0)
        self.assertEqual( c.last_trained_epoch(), 0)

    def test_historyplotter(self):
        pass


if __name__ == '__main__':
    unittest.main()
