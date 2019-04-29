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

    def test_json(self):
        path = 'temp/test.json'
        data = { 'key' : path }
        moonhill.io.write_json(path, data)
        r = moonhill.io.read_json(path)
        self.assertEqual(path, r['key'])

if __name__ == '__main__':
    unittest.main()
