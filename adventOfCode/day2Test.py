import unittest
from adventOfCode.day2 import *

sample = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

real = '''197-407,262128-339499,557930-573266,25-57,92856246-93001520,2-12,1919108745-1919268183,48414903-48538379,38342224-38444598,483824-534754,1056-1771,4603696-4688732,75712519-75792205,20124-44038,714164-782292,4429019-4570680,9648251-9913729,6812551522-6812585188,58-134,881574-897488,648613-673853,5261723647-5261785283,60035-128980,9944818-10047126,857821365-857927915,206885-246173,1922-9652,424942-446151,408-1000'''

class MyTestCase(unittest.TestCase):
    def test_twoDigitsTwoInvalid(self):
        self.assertEqual(33, invalid_sum('11-22'))
    def test_twoDigitsOneInvalid(self):
        self.assertEqual(99, invalid_sum('95-115'))
    def test_moreThanTwoDigits(self):
        self.assertEqual(222222, invalid_sum('222220-222224'))
    def test_noneInvalid(self):
        self.assertEqual(0, invalid_sum('1698522-1698528'))
    def test_sample(self):
        self.assertEqual(1227775554, invalid_sum(sample))
    def test_real(self):
        self.assertEqual(19128774598, invalid_sum(real))
    def test_three9s(self):
        self.assertEqual(999, invalid_sum('998-1000', True))
    def test_singleSum2(self):
        self.assertEqual(999+1010, invalid_sum('998-1012', True))
    def test_sample2(self):
        self.assertEqual(4174379265, invalid_sum(sample, True))
    def test_real2(self):
        self.assertEqual(21932258645, invalid_sum(real, True))



if __name__ == '__main__':
    unittest.main()
