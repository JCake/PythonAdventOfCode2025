import unittest
from adventOfCode.day8 import *

sample = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

input_file = open('adventOfCode/day8.txt','r')
real_str = input_file.read()
input_file.close()

class MyTestCase(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(40, circuit(sample, 10))

    def test_real(self):
        self.assertEqual(181584, circuit(real_str, 1000))

    def test_max_sample(self):
        self.assertEqual(25272, max_circuit(sample))

    def test_max_real(self):
        self.assertEqual(8465902405, max_circuit(real_str))


if __name__ == '__main__':
    unittest.main()
