import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_duplas
        undertest = __import__(module)
        remove_duplas = getattr(undertest, 'remove_duplas', None)

    def test_example(self):
        lista = [1, 1, 20, 20, 5, 1]
        assert remove_duplas(lista) == None
        assert lista == [1, 1, 5, 1]

    def test_exemplo2(self):
        lista = [-10, 12, -10, 12, -10, -10]
        assert remove_duplas(lista) == None
        assert lista == [-10, -10, -10, -10]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
