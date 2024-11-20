import unittest
from MétodoBisección.biseccion import metodo_biseccion

class TestBiseccion(unittest.TestCase):

    def test_biseccion(self):
        def func(x):
            return x**3 - 4*x**2 - 7
        a = 1
        b = 10
        tol = 0.0001

        expected_root = 7.096
        root, iterations = metodo_biseccion(func, a, b, tol)

        self.assertAlmostEqual(root, expected_root, places=3)
        self.assertGreater(iterations, 0)

        print(f"La raíz aproximada es: {root}")
        print(f"Número de iteraciones: {iterations}")

if __name__ == "__main__":
    unittest.main()

