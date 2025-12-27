import unittest
from adventOfCode.day4 import *

sample = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

input_file = open('adventOfCode/day4.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(0, accessible_paper(''))

    def test_one_roll(self):
        self.assertEqual(1, accessible_paper('@'))

    def test_all_grid(self):
        self.assertEqual(4, accessible_paper(
'''@@@
@@@
@@@'''))

    def test_sample(self):
        self.assertEqual(13, accessible_paper(sample))

    def test_real(self):
        self.assertEqual(1424, accessible_paper(real_str))

    def test_sample_continuing(self):
        self.assertEqual(43, accessible_paper_continuing(sample))

    def test_real_continuing(self):
        self.assertEqual(8727, accessible_paper_continuing(real_str))


if __name__ == '__main__':
    unittest.main()
