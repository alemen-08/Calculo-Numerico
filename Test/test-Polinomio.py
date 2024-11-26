import unittest
import sympy as sp
from PolinomioTaylor import taylor_series

class TestPolinomioTaylor(unittest.TestCase):
    def test_taylor_series_sin(self):
        x = sp.symbols('x')
        func = sp.sin(x)
        x0 = 0
        n = 5

        taylor_poly = taylor_series(func, x0, n)
        expected_poly = x - (x**3)/6 + (x**5)/120

        self.assertEqual(taylor_poly, expected_poly)

    def test_taylor_series_cos(self):
        x = sp.symbols('x')
        func = sp.cos(x)
        x0 = 0
        n = 4

        taylor_poly = taylor_series(func, x0, n)
        expected_poly = 1 - (x**2)/2 + (x**4)/24

        self.assertEqual(taylor_poly, expected_poly)

    def test_taylor_series_exp(self):
        x = sp.symbols('x')
        func = sp.exp(x)
        x0 = 0
        n = 4

        taylor_poly = taylor_series(func, x0, n)
        expected_poly = 1 + x + (x**2)/2 + (x**3)/6 + (x**4)/24

        self.assertEqual(taylor_poly, expected_poly)

if __name__ == "__main__":
    unittest.main()
