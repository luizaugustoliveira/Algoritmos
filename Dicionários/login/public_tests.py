import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
login = getattr(undertest, 'login', None)

class PublicTests(unittest.TestCase):
   
    def test_exemplo(self):
        dados = {1313:['j@gmail.com'], 1226:['e@cc.com', 'd@cc.com'], 1507:['pedro@cc.com'] }
        assert login(dados, 'd@cc.com', 1313) == False
        assert login(dados, 'd@cc.com', 1226) == True
        assert login(dados, 'joao@gmail.com', '123') == False

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
