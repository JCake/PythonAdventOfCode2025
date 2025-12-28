import unittest
from adventOfCode.day7 import *

sample = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

input_file = open('adventOfCode/day7.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_no_splitting(self):
        self.assertEqual(0, splitter('.S.'))

    def test_one_split(self):
        self.assertEqual(1, splitter(
'''..S..
.....
..^..
.....
.....
'''))

    def test_one_split_one_missed(self):
        self.assertEqual(1, splitter(
'''..S..
.....
..^..
....^
.....
'''))

    def test_sample(self):
        self.assertEqual(21, splitter(sample))

    def test_timelines_sample(self):
        self.assertEqual(40, timelines(sample))

    def test_real(self):
        full_result = full_split(real_str)
        self.assertEqual(1667, full_result[0])
        self.assertEqual(-1, full_result[1])




if __name__ == '__main__':
    unittest.main()
