#Supacharn Kaowanan 653380026-4 Section1

import unittest
from source import CountClump as CountClump

class TestByC_DC_Coverage(unittest.TestCase):
    def test_TC01(self):
        result = CountClump.CountClump.count_clumps([0])
        self.assertEqual(result, 0)

    def test_TC02(self):
        result = CountClump.CountClump.count_clumps([1,2,3])
        self.assertEqual(result, 0)

    def test_TC03(self):
        result = CountClump.CountClump.count_clumps([1,1,2,3])
        self.assertEqual(result, 1)

    def test_TC04(self):
        result = CountClump.CountClump.count_clumps(None)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
