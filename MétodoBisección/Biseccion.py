def metodo_biseccion(func, a, b, tol):
    """
    Metodo de biseccion para encontrar la raiz de una funcion.

    Parámetros:
    func: La funcion de la cual encontrar la raiz.
    a: Punto a.
    b: Punto b.
    tol: margen de error permitido.

    Retorna:
    Una tupla que contiene la raiz aproximada y el numero de iteraciones realizadas.
    """
    if func(a) * func(b) >= 0:
        print("La funcion debe cambiar de signo en el intervalo [a, b].")
        return None
    
    iter_count = 0
    while (b - a) / 2.0 > tol:
        iter_count += 1
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:
            return midpoint, iter_count
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2.0, iter_count

# testing...
def func(x):
    return x**3 - 4*x**2 - 7

a = 1
b = 10
tol = 0.0001

root, iterations = metodo_biseccion(func, a, b, tol)
print(f"La raiz aproximada es: {root}")
print(f"Numero de iteraciones: {iterations}")
