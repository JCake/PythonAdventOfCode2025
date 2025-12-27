import unittest
from adventOfCode.day5 import *

sample = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

input_file = open('adventOfCode/day5.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(3, ingredient_count(sample))

    def test_real(self):
        self.assertEqual(558, ingredient_count(real_str))

    def test_sample_all(self):
        self.assertEqual(14, possible_fresh_count(sample))

    def test_real_all(self):
        self.assertEqual(344813017450467, possible_fresh_count(real_str))

if __name__ == '__main__':
    unittest.main()
