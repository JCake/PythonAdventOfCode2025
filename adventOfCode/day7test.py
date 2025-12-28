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
        self.assertEqual(0, splitter('.S.').splits)

    def test_one_split(self):
        self.assertEqual(1, splitter(
'''..S..
.....
..^..
.....
.....
''').splits)

    def test_one_split_one_missed(self):
        self.assertEqual(1, splitter(
'''..S..
.....
..^..
....^
.....
''').splits)

    def test_sample(self):
        full_result = splitter(sample)
        self.assertEqual(21, full_result.splits)
        self.assertEqual(40, full_result.timelines)


    def test_real(self):
        full_result = splitter(real_str)
        self.assertEqual(1667, full_result.splits)
        self.assertEqual(62943905501815, full_result.timelines)




if __name__ == '__main__':
    unittest.main()
