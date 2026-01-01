import unittest
from adventOfCode.day11 import *

sample = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

input_file = open('adventOfCode/day11.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_no_paths_empty_string(self):
        self.assertEqual(0, paths(''))

    def test_one_direct_path(self):
        self.assertEqual(1, paths('you: out'))

    def test_one_indirect_path(self):
        self.assertEqual(1, paths(
'''you: aaa
aaa: bbb
bbb: out'''
        ))

    def test_two_overlapping_paths(self):
        self.assertEqual(2, paths(
'''you: aaa bbb
aaa: bbb
bbb: out'''
))

    def test_a_sample(self):
        self.assertEqual(5, paths(sample))

    def test_real(self):
        self.assertEqual(585, paths(real_str))

    def test_part2_sample(self):
        self.assertEqual(2, restricted_paths('''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''))

    def test_part2_real(self):
        self.assertEqual(585, restricted_paths(real_str))


if __name__ == '__main__':
    unittest.main()
