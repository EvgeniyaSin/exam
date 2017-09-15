import unittest

from count import Ten


class TestCount(unittest. TestCase):
    def setUp(self):
        self.res = Ten()

    def test_positive(self):
        self.assertEqual(10, self.res.summ(0,10))

    def test_positive_1(self):
        self.assertEqual(9, self.res.summ(3, 6))

    def test_negative(self):
        self.assertNotEqual(5, self.res.summ(6, 1))

    def test_negative_1(self):
        self.assertEqual(-1, self.res.summ(-1, 11))

    def test_negative_2(self):
        self.assertEqual(-1, self.res.summ(0, 11))

    def test_negative_2(self):
        self.assertEqual(-1, self.res.summ(-10, 1))

if __name__=='__main__':
    unittest.main()
