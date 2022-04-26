import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global indexa
        undertest = __import__(module)
        indexa = getattr(undertest, 'indexa', None)

    def test_exemplo(self):
        indice = {}
        indexa("Jose Silva", indice)
        assert indice == {
            "jose": ["Jose Silva"],
            "silva": ["Jose Silva"]
        }

        indexa("Joao Silva", indice)
        assert indice == {
            "joao": ["Joao Silva"],
            "jose": ["Jose Silva"],
            "silva": ["Jose Silva", "Joao Silva"]
        }

        indexa("Jose Pereira", indice)
        assert indice == {
            "joao": ["Joao Silva"],
            "jose": ["Jose Silva", "Jose Pereira"],
            "silva": ["Jose Silva", "Joao Silva"],
            "pereira": ["Jose Pereira"]
        }

        indexa("Joao Silva", indice)
        assert indice == {
            "joao": ["Joao Silva"],
            "jose": ["Jose Silva", "Jose Pereira"],
            "silva": ["Jose Silva", "Joao Silva"],
            "pereira": ["Jose Pereira"]
        }

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
