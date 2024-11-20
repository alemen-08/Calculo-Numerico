import sympy as sp

def taylor_series(func, x0, n):
    """
    Metodo del polinomio de Taylor para aproximar una funcion.

    Parametros:
    func: La funcion la cual se debe calcular el polinomio de Taylor.
    x0: El punto alrededor del cual se calcula el polinomio de Taylor.
    n: El orden del polinomio de Taylor.

    Retorna:
    El polinomio de Taylor de orden n.
    """
    x = sp.symbols('x')
    taylor_poly = 0

    for i in range(n + 1):
        taylor_poly += (func.diff(x, i).subs(x, x0) / sp.factorial(i)) * (x - x0)**i

    return taylor_poly

# testing...
x = sp.symbols('x')
func = sp.sin(x)  
x0 = 0  
n = 5  

taylor_poly = taylor_series(func, x0, n)
print(f"El polinomio de Taylor de orden {n} es: {taylor_poly}")
