import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global normaliza_matriz
        undertest = __import__(module)
        normaliza_matriz = getattr(undertest, 'normaliza_matriz', None)

    def test_simples(self):
        m = [ [20, 5, 3], [ 6, 4, 2], [ 3, 1, 9], ]
        normaliza_matriz(m)
        assert m == [ [ 15,  0, -2], [  1, -1, -3], [ -2, -4,  4], ]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
