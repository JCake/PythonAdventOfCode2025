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

    # 1518085800 is too low
    # 1979617678 is too high
    def test_real_limited(self):
        self.assertEqual(4748769124, limited_area(real_str))


    def test_areas_in_range(self):
        areas = areas_in_range(real_str, 1518085800, 1979617678)
        print(areas)
        self.assertEqual(5, len(areas))

if __name__ == '__main__':
    unittest.main()
