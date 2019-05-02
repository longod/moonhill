import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.nn
import keras

class TestModel(unittest.TestCase):
    def test_alexnet(self):
        self.assertNotEqual(moonhill.nn.models.alexnet_1d(), None)
        self.assertNotEqual(moonhill.nn.models.alexnet_1d(keras.models.Sequential()), None)

    def test_vgg16(self):
        self.assertNotEqual(moonhill.nn.models.vgg16_1d(), None)
        self.assertNotEqual(moonhill.nn.models.vgg16_1d(keras.models.Sequential()), None)

if __name__ == '__main__':
    unittest.main()
