import unittest
from adventOfCode.day1 import *

oneFromMultiple = '''L55
R5'''

exampleStr = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

inputFile = open('adventOfCode/day1a.txt','r')
realStr = inputFile.read()
inputFile.close()

class MyTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, password('L2'))
    def test_oneLeft(self):
        self.assertEqual(1, password('L50'))
    def test_oneFromMultiple(self):
        self.assertEqual(1, password(oneFromMultiple))
    def test_example(self):
        self.assertEqual(3, password(exampleStr))
    def test_real(self):
        self.assertEqual(984, password(realStr))
    def test_example2(self):
        self.assertEqual(6, password(exampleStr, True))
    def test_giantSpin(self):
        self.assertEqual(10, password('R1000', True))
    def test_real2(self):
        self.assertEqual(5657, password(realStr, True))


if __name__ == '__main__':
    unittest.main()
