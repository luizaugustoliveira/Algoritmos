import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global primos_ate
        undertest = __import__(module)
        primos_ate = getattr(undertest, 'primos_ate', None)

    def test_1(self):
        assert primos_ate(10) == [2, 3, 5, 7]
        assert primos_ate(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
