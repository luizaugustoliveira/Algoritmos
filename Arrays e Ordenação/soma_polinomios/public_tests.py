import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_polinomios
        undertest = __import__(module)
        soma_polinomios = getattr(undertest, 'soma_polinomios', None)

    def test_exemplo(self):
        p1 = [3, 4, -5]
        p2 = [5, 0, 0, 0, 2, 0, -1]
        assert soma_polinomios(p1, p2) == [5, 0, 0, 0, 5, 4, -6]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
