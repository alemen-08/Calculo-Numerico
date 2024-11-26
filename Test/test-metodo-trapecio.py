import unittest
from MetodoTrapecio import metodo_trapecio

class TestMetodoTrapecio(unittest.TestCase):
    def test_metodo_trapecio(self):
        def func(x):
            return x**2
        
        a = 0
        b = 1
        n = 1000
        
        result = metodo_trapecio(func, a, b, n)
        expected_result = 1/3  #La integral de x^2 en [0, 1] es 1/3
        
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_metodo_trapecio_linear(self):
        def func(x):
            return 2*x + 1
        
        a = 0
        b = 1
        n = 1000
        
        result = metodo_trapecio(func, a, b, n)
        expected_result = 2  #La integral de 2*x + 1 en [0, 1] es 2
        
        self.assertAlmostEqual(result, expected_result, places=2)

if __name__ == "__main__":
    unittest.main()
