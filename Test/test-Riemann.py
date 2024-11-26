import unittest
import numpy as np
from IntegralRiemann import integral_riemann  

class TestRiemannSum(unittest.TestCase):
    def test_riemann_sum(self):
        def func(x):
            return x**2
        
        a = 0
        b = 1
        n = 1000
        
        integral = integral_riemann(func, a, b, n)
        expected_value = 1/3                    # La integral de x^2 en [0, 1] es 1/3
        
        self.assertAlmostEqual(integral, expected_value, places=2)
    
    def test_integral_riemann_linear(self):
        def func(x):
            return 2*x + 1
        
        a = 0
        b = 1
        n = 1000
        
        integral = integral_riemann(func, a, b, n)
        expected_value = 2                      # La integral de 2*x + 1 en [0, 1] es 2
        
        self.assertAlmostEqual(integral, expected_value, places=2)

if __name__ == "__main__":
    unittest.main()
