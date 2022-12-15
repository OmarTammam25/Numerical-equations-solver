import unittest
from Gauss import Gauss
class testGauss(unittest.TestCase):

    def test1(self):
        a = [[1, 1, -1], [6, 2, 2], [-3, 4, 1]]
        b = [-3, 2, 1]
        gauss = Gauss(a,b)
        x = [-0.25, -0.5, 2.25]
        self.assertEqual(gauss.gaussElimination(), x)

    def test2(self):
        a = [[8, 4, -1], [-2, 3, 1], [2, -1, 6]]
        b = [11, 4, 7]
        gauss = Gauss(a, b)
        x = [0.783, 1.472, 1.151]
        self.assertEqual(gauss.gaussElimination(), x)

    def test3(self):
        a = [[2, 3, 1], [4, 1, 4], [3, 4, 6]]
        b = [-4, 9, 0]

        x = [2.0, -3.0, 1.0]

