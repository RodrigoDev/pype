import unittest
from core import Pype

class PypeTestCase1(unittest.TestCase):
    def setUp(self):
        pass

    def testPypeReturnAPipe(self):
        assert "[|===|]" == Pype().run()

if __name__ == '__main__':
    unittest.main()