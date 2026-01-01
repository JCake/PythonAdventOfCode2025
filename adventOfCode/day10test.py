import unittest
from adventOfCode.day10 import *

sample = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

input_file = open('adventOfCode/day10.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_list_compare(self):
        self.assertEqual([False, True, True, False], [False, True, True, False])

    def test_a_sample(self):
        self.assertEqual(7, min_presses(sample))

    # currently takes > 8 sec
    def test_real(self):
        self.assertEqual(401, min_presses(real_str))

    def test_a_sample_joltage(self):
        self.assertEqual(33, min_presses_joltage(sample))

    def test_real_joltage(self):
        self.assertEqual(33, min_presses_joltage(real_str))

if __name__ == '__main__':
    unittest.main()
