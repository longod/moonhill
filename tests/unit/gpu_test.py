import unittest
import os, sys
sys.path.append(os.getcwd())
import moonhill.gpu

# move anywhere
# callableObj = function name
def assertNotRaise(self, callableObj, *args, **kwargs):
    try:
        callable(*args, **kwargs)
    except:
        self.fail('{} raised: '.format( repr(sys.exc_info()[0]) ) )
unittest.TestCase.assertNotRaise = assertNotRaise

class TestGPU(unittest.TestCase):
    def test_query(self):
        self.assertIsNotNone( moonhill.gpu.query() )

    def test_memory_allocation(self):
        self.assertNotRaise( moonhill.gpu.memory_allocation_allow_groth, [True] )
        self.assertNotRaise( moonhill.gpu.memory_allocation_allow_groth, [False] )
        self.assertNotRaise( moonhill.gpu.memory_allocation_fraction, [0.5] )
        self.assertNotRaise( moonhill.gpu.memory_allocation_mb, [64] )
        # I expect return any exceptions below args, but tensorflow return no exception.
        self.assertNotRaise( moonhill.gpu.memory_allocation_fraction, [0] )
        self.assertNotRaise( moonhill.gpu.memory_allocation_mb, [0] )

if __name__ == '__main__':
    unittest.main()
