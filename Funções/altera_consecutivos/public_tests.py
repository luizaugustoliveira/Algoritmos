import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global inverte2a2
        undertest = __import__(module)
        inverte2a2 = getattr(undertest, 'inverte2a2', None)

    def test_basico(self):
        seq = [10, 20, 30, 40, 50, 60]
        inverte2a2(seq)
        assert seq == [20, 10, 40, 30, 60, 50]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
