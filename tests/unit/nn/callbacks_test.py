import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.nn
import keras

class TestCallback(unittest.TestCase):
    def test_persistent(self):
        c = moonhill.nn.callbacks.PersistentHistory()
        # initialize of super's constructor
        self.assertIsNone(c.model)
        self.assertIsNone(c.validation_data)
        # integration testでやらないと…
        self.assertEqual( c.initial_epoch(), 0)
        self.assertEqual( c.epochs(1), 1)

if __name__ == '__main__':
    unittest.main()
