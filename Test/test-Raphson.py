import unittest
from NewtonRaphson import newton_raphson_metodo

class TestNewtonRaphson(unittest.TestCase):
    def test_newton_raphson_metodo(self):
        def func(x):
            return x**3 - 4*x**2 - 7

        def deriv(x):
            return 3*x**2 - 8*x

        x0 = 5
        tol = 0.0001
        max_iter = 100

        expected_root = 7.0  #Valor de la precision esperada.
        root, iterations = newton_raphson_metodo(func, deriv, x0, tol, max_iter)

        #Verifica si la raiz calculada es cercana al valor esperado.
        self.assertAlmostEqual(root, expected_root, delta=tol)
        
        #Verifica que se haya realizado al menos una iteracion.
        self.assertGreater(iterations, 0)

        print(f"La raíz aproximada es: {root}")
        print(f"Número de iteraciones: {iterations}")

    def test_newton_raphson_zero_derivative(self):
        def func(x):
            return x**3 - 3*x**2 + 2*x

        def deriv(x):
            return 3*x**2 - 6*x + 2  #Derivada se vuelve cero en x=1

        x0 = 1
        tol = 0.0001
        max_iter = 100

        root, iterations = newton_raphson_metodo(func, deriv, x0, tol, max_iter)

        #Verifica que el metodo no puede continuar cuando la derivada es cero.
        self.assertIsNone(root)
        self.assertGreater(iterations, 0)

    def test_newton_raphson_max_iterations(self):
        def func(x):
            return x**3 - 4*x**2 - 7

        def deriv(x):
            return 3*x**2 - 8*x

        x0 = 5
        tol = 0.0001
        max_iter = 1  #Fuerza a alcanzar el numero maximo de iteraciones.

        root, iterations = newton_raphson_metodo(func, deriv, x0, tol, max_iter)

        #Verifica que el metodo se detiene despues del numero maximo de iteraciones.
        self.assertNotEqual(iterations, 0)
        self.assertEqual(iterations, max_iter)

if __name__ == "__main__":
    unittest.main()
