import unittest
from adventOfCode.day9 import *

sample = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

input_file = open('adventOfCode/day9.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_a_sample(self):
        self.assertEqual(50, max_area(sample))

    def test_real(self):
        self.assertEqual(4748769124, max_area(real_str))

    def test_a_sample_limited(self):
        self.assertEqual(24, limited_area(sample))

    # 4629351648 is too high
    # 1518085800 is too low
    def test_real_limited(self):
        self.assertEqual(4748769124, limited_area(real_str))


if __name__ == '__main__':
    unittest.main()
