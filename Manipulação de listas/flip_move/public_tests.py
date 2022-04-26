import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global flipmove
        undertest = __import__(module)
        flipmove = getattr(undertest, 'flipmove', None)

    def test_do_enunciado_1(self):
        lista = [5, 8, 3, 7, 1, 6, 4, 9, 2]
        flipmove(lista, 4)
        assert lista == [1, 6, 4, 9, 2, 7, 3, 8, 5], lista

    def test_do_enunciado_2(self):
        lista2 = [5, 8, 3, 7, 1, 6, 4, 9, 2]
        flipmove(lista2, 2)
        assert lista2 == [3, 7, 1, 6, 4, 9, 2, 8, 5]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
