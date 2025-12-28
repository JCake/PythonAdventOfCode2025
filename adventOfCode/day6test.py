import unittest
from adventOfCode.day6 import *

sample = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

input_file = open('adventOfCode/day6.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(4277556, math(sample))

    def test_real(self):
        self.assertEqual(4580995422905, math(real_str))

if __name__ == '__main__':
    unittest.main()
