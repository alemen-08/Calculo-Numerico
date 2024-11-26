import unittest
from Biseccion import metodo_biseccion

class TestBiseccion(unittest.TestCase):
    def test_metodo_biseccion(self):
        def func(x):
            return x**3 - 4*x**2 - 7
        
        a = 1
        b = 10
        tol = 0.0001

        expected_root = 7.096 #Valor esperado de la raiz con una precision aceptable.
        root, iterations = metodo_biseccion(func, a, b, tol)

        #Verifica si la raiz calculada es cercana al valor esperado.
        self.assertAlmostEqual(root, expected_root, places=3)
        
        #Verifica que se haya realizado al menos una iteracion.
        self.assertGreater(iterations, 0)

        print(f"La raiz aproximada es: {root}")
        print(f"Numero de iteraciones: {iterations}")
        

    def test_no_sign_change(self):
        def func(x):
            return x**2 + 1  #No hay cambio de signo en el intervalo [1, 2]
        with self.assertRaises(ValueError):
            metodo_biseccion(func, 1, 2, 0.0001)
    
    def test_exact_root(self):
        def func(x):
            return (x - 3)**2
        root, iterations = metodo_biseccion(func, 2, 4, 0.0001)
        self.assertAlmostEqual(root, 3.0, places=3)

if __name__ == "__main__":
    unittest.main()
