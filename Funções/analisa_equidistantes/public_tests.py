import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global analisa_equidistantes
        undertest = __import__(module)
        analisa_equidistantes = getattr(undertest, 'analisa_equidistantes', None)

    def test_exemplo_1(self):
        assert analisa_equidistantes([3,5,15,2,4,30,10,6]) == [3,5,15,8]

    def test_exmplo_2(self):
        assert analisa_equidistantes([1,9,10,18,7]) == [7,3,10]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
