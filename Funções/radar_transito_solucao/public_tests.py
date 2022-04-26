# coding: utf-8

import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global radar_transito
        undertest = __import__(module)
        radar_transito = getattr(undertest, 'radar_transito', None)

    def test_basico_1(self):
        assert radar_transito(80.0, 0.1) == ["Ok", 0.0]
        
    def test_basico_2(self):
        assert radar_transito(80.0, 0.085) == ["Leve", 87.5]
        
    def test_basico_3(self):        
        assert radar_transito(80.0, 0.07) == ["Média", 127.5]
        
    def test_basico_4(self):
        assert radar_transito(80.0, 0.05) == ["Grave", 577.5]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
