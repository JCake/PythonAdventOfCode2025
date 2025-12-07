import unittest
from adventOfCode.day3 import *

sample = '''987654321111111
811111111111119
234234234234278
818181911112111'''

input_file = open('adventOfCode/day3.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(357, joltage(sample))

    def test_real(self):
        self.assertEqual(17524, joltage(real_str))

    def test_easyLine2(self):
        self.assertEqual(987654321111, extra_joltage('987654321111111'))

    def test_useLastDigit2(self):
        self.assertEqual(811111111119, extra_joltage('811111111111119'))

    def test_notFirstDigit2(self):
        self.assertEqual(434234234278, extra_joltage('234234234234278'))

    def test_sample2(self):
        self.assertEqual(3121910778619, extra_joltage(sample))

    def test_real2(self):
        self.assertEqual(173848577117276, extra_joltage(real_str))




if __name__ == '__main__':
    unittest.main()
