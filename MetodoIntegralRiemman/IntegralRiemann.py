import numpy as np

def riemann_sum(func, a, b, n):
    """
    Calcula la suma de Riemann de una funcion en un intervalo [a, b] utilizando n sub intervalos.

    Parametros:
    func: La funcion a integrar.
    a: Punto a.
    b: Punto b.
    n: El numero de sub intervalos.

    Retorna:
    La aproximacion de la integral.
    """
    dx = (b - a) / n
    total_sum = 0.0

    for i in range(n):
        x = a + i * dx
        total_sum += func(x) * dx

    return total_sum

# Test...
def example_func(x):
    return x**2

a = 0
b = 1
n = 1000

integral = riemann_sum(example_func, a, b, n)
print(f"La integral aproximada es: {integral}")
