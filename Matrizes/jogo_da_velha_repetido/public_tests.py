import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global jogo_da_velha
        undertest = __import__(module)
        jogo_da_velha = getattr(undertest, 'jogo_da_velha', None)
    
    def test_publico1(self):
        jogo1 = [['O', 'O', 'X'],['X', 'O', 'O'],['O', 'O', 'X'] ]
        assert jogo_da_velha(jogo1) == 'O ganhou'

    def test_publico2(self):
        jogo2 = [['O', 'X', 'X'],['X', 'X', 'O'],['O', 'O', 'X'] ]
        assert jogo_da_velha(jogo2) == 'Ninguem ganhou'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
